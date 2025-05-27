from django.contrib import admin
from .models import *

# Register your models here.

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

admin.site.register(Member, memberAdmin)
admin.site.register(Event, eventAdmin)
admin.site.register(Roll, rollAdmin)
admin.site.register(Committee, committeeAdmin)
