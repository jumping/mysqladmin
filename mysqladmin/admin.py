#!/usr/bin/env python
# -*- coding: UTF8 -*-
# 
#   Jumping Qu @ BPO
#
#vim: ts=4 sts=4 et sw=4
#
from django.contrib import admin
from mysqladmin.models import DbHost,DbInstance,DbRds,InstanceHistory,InstanceInfo,UserDb,UserInfo

admin.site.register(DbHost)
admin.site.register(DbInstance)
admin.site.register(DbRds)
admin.site.register(InstanceHistory)
admin.site.register(InstanceInfo)
admin.site.register(UserDb)
admin.site.register(UserInfo)

