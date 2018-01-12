# !/user/bin/env python 
# -*- coding: utf-8 -*-
__author__ = 'dlh'
__date__ = '2018/1/2 14:27'
import xadmin
from .models import Contact


class ContactAdmin(object):
    list_display = ['name', 'phone', 'openId']
    search_fields = ['name', 'phone', 'openId']
    list_filter = ['name', 'phone', 'openId']


xadmin.site.register(Contact, ContactAdmin)
