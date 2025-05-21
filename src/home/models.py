import datetime
import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.


class Committee(models.Model):
    """
    Model storing committee info
    Referenced by the members and the events models
    """
    page_name = models.SlugField(primary_key=True)
    full_name = models.CharField(max_length=100)
    discord = models.CharField(max_length=50)  # TODO make larger if needed
    descriptor = models.TextField()
    members = models.ManyToManyField(
        'Member',
        through='Roll',
        through_fields=('committee', 'person')
    )
    description = models.TextField()

    def __str__(self):
        """Human readable representation"""
        return self.full_name

    def get_associates(self):
        return self.members.all()

    def get_officers(self):
        """
        get the list of all officers
        running the committee
        """
        return self.objects.filter('rollname')



class Event(models.Model):
    """
    Model for all of the minor events.
    NOTE: this does not include events who have a dedicated committee,
    meaning MID, Lab Expo, and BE day.
    TODO: Check if that note is true
    """
    start_date = models.DateTimeField('Event Start')
    end_date = models.DateTimeField('Event End')
    name = models.CharField(max_length=200)
    flyer = models.ImageField(upload_to='')  # TODO make Path object to get the upload location
    # /uploads/events/<event_name>
    description = models.TextField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    managing_committee = models.ForeignKey(Committee, on_delete=models.CASCADE)


class Member(models.Model):
    """
    Model to store all information about members
    Anything other than the email can be null,
    and not null constraints are enforced for officers and
    subleads
    """
    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    member_since = models.DateField(default=timezone.now())
    linkedin = models.URLField(blank=True)
    portfolio = models.URLField(blank=True)  # Website or other link to personal info that isn't linkedin
    github = models.URLField(blank=True)  # Presumably the only person who will use this is you :)
    # But who knows, maybe a binfo person will want it
    headshot = models.ImageField(upload_to=None, blank=True)  #  TODO add upload destination
    active = models.BooleanField(default=True)
    eboard = models.BooleanField(default=False)

class Roll(models.Model):
    """
    Intermediary relation used to map
    each member to their respective committee,
    including the roll the possess in that
    committee
    TODO: add specific options for which rolls are
    possible. This might not
    be a constraint of this table, but roll names
    (for each sublead, offficer, and eboard member)
    will need to be stored somewhere, and this is
    a part of that relation
    TODO: Add constraint to ensure any
    relation with an officer/sublead role requires that certain
    fields are not empty before saving
    """
    ROLLS = {
        'sl': 'Sublead',
        'off': 'Officer',
        'mbr': 'Member'
    }
    committee = models.ForeignKey(Committee, on_delete=models.PROTECT, related_name="member_of")
    person = models.ForeignKey(Member, on_delete=models.PROTECT, related_name="member")
    roll_name = models.CharField(choices=ROLLS, default='mbr')
    # TODO: add unique constraint for any pair of (committee, roll) to ensure
    # no one is in the same committee twice
