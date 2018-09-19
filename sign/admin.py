# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from django.contrib import admin
from sign.models import Event, Guest
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['id','name','status','address','start_time']
    search_fields = ['name'] #搜索组
    list_filter = ['status'] #过滤器

class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname','phone','email','sign','create_time','event']
    search_fields = ['realname','phone'] #搜索组
    list_filter = ['sign'] #过滤器
admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)
