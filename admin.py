from django.contrib import admin

from django.contrib.auth.models import Group

from .models import *
from watchman.models import *


# for admin title 
admin.site.site_header = 'Admin - Digital Society'
admin.site.index_title = 'Digital Society Administration'
admin.site.site_url='http://127.0.0.1:8000/chairman/'

# modify models 
class NoticeA(admin.ModelAdmin):
    exclude = ('created_date', 'updated_date')
    list_filter= ('created_date',)

class MemberA(admin.ModelAdmin):
    list_display = ('firstname','email','profile_picture')
    search_fields = ("firstname__startswith", ) # search 

# # Register your models here.
admin.site.register(MemberDetails)
admin.site.register(Chairman)
admin.site.register(Member,MemberA)
admin.site.register(Events)
admin.site.register(Watchman)
admin.site.register(Notice,NoticeA)

#admin.site.unregister(Group)

