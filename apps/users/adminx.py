# !/user/bin/env python 
# -*- coding: utf-8 -*-
__author__ = 'dlh'
__date__ = '2018/1/2 12:29'

import xadmin
from xadmin import views
from .models import Area

from contact.models import Contact


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = u'入户管理系统'
    site_footer = u'入户管理系统'
    menu_style = 'accordion'

class AreaAdmin(object):
    list_display = ['area_name', 'ordering']
    search_fields = ['area_name', 'ordering']
    list_filter = ['area_name', 'ordering']





xadmin.site.register(Area, AreaAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
