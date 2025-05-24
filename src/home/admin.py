from django.contrib import admin
from .models import *

# Register your models here.

class committeeAdmin(admin.ModelAdmin):
    # This should be fairly static
    # but should certainly allow easy
    # changing of subleads for officers
    # and changing officers for eboard
    pass

class memberAdmin(admin.ModelAdmin):
    # Ideally this will be automated but manual controll
    # Should be needed
    pass

class eventAdmin(admin.ModelAdmin):
    # NOTE: this might be different since
    # event adding is different
    pass

admin.site.register(Committee, committeeAdmin)
admin.site.register(Member, memberAdmin)
admin.site.register(Event, eventAdmin)
