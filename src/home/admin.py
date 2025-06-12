from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError

from .models import *

# Register your models here.


# admin Site forms and registration systems


class UserCreationForm(forms.ModelForm):
    """
    Form for making new users. Includes all of the relevant
    fields for this process
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Member
        fields = ['email']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Member
        fields = '__all__'


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['email', 'name']
    list_filter = ['is_superuser', 'is_staff']
    # TODO: see if we can add a filter on the Rolls join
    fieldsets = [
        (None, {'fields': ['email', 'password']}),
        ('Personal Info', {'fields': ['name', 'about', 'headshot']}),
        ('Links', {'fields': ['linkedin', 'portfolio', 'github']}),
        ('Admin', {'fields': [
            'eboard',
            'is_active',
            'is_superuser',
            'is_staff'
        ]})
    ]
    add_fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['email', 'password1', 'password2']
            }
        )
    ]
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = []


class rollAdmin(admin.ModelAdmin):
    pass

class memberAdmin(admin.ModelAdmin):
    # Ideally this will be automated but manual control
    # Should be needed
    list_display = ['email', 'name']

class eventAdmin(admin.ModelAdmin):
    # NOTE: this might be different since
    # event adding is different
    list_display = ['name', 'start_date']

class committeeAdmin(admin.ModelAdmin):
    # NOTE: this will be removed for final
    # production, but for testing having
    # an interface to add committees will be
    # helpfull
    pass

admin.site.register(Member, UserAdmin)
admin.site.register(Event, eventAdmin)
admin.site.register(Roll, rollAdmin)
admin.site.register(Committee, committeeAdmin)
