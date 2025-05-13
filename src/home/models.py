from django.db import models

# Create your models here.

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
    managing_committee = models.ForeignKey(committee, on_delete=models.CASCADE)

class Committee(models.Model):
    """
    Model storing committee info
    Referenced by the members and the events models
    """
    page_name = models.SlugField(primary_key=True)
    full_name = models.CharField(max_length=100)
    discord = models.CharField(max_length=50)  # TODO make larger if needed
    descriptor = models.TestField()

class Member(models.Model):
    """
    Model logging all members.
    Logs primarily emails (Primary key), but
    will also track other info.
    """
    email = models.EmailField(primary_key=True)
