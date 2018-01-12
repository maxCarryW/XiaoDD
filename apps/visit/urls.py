# !/user/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'dlh'
__date__ = '2018/1/2 14:50'

from django.conf.urls import url
from .views import ContactListView, ContactCheckView
from .views import IndexView, InsertListView, VisitListView

urlpatterns = [
    url(r'', IndexView.as_view(), name='index'),
    url(r'^InsertList', InsertListView.as_view(), name='InsertList'),
    url(r'^VisitList', VisitListView.as_view(), name='VisitList'),

    # 后台管理模块
    url(r'^list', ContactListView.as_view(template_name="manage/contact_list.html"), name='list'),
    url(r'^check', ContactCheckView.as_view(), name='check'),

]
