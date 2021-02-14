from django.contrib import admin
from .models import *
from watchman.models import *

admin.site.site_url='http://127.0.0.1:8000/chairman/'

# for admin theme customization 

"""
pip install django-admin-interface

-> add below apps in settings.py 

'admin_interface',
'colorfield',

"""

class MemberAdmin(admin.ModelAdmin):
    #exclude = ('created_date', 'updated_date')
    list_display= ('firstname','lastname','email','profile_picture','status',)
    list_display_links= ('firstname',)
    list_editable= ('status','lastname')
    list_per_page = 5
    search_fields= ('firstname',)
    list_filter = ('firstname',)    

# Register your models here.
admin.site.register(MemberDetails)
admin.site.register(Chairman)
admin.site.register(Member,MemberAdmin)
admin.site.register(Notice)
admin.site.register(Gallary)
admin.site.register(VideoGallary)
admin.site.register(Event)
admin.site.register(Watchman)
admin.site.register(Maintenance)
admin.site.register(Complaint)
admin.site.register(Visitor)