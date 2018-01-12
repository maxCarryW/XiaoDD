# !/user/bin/env python 
# -*- coding: utf-8 -*-
__author__ = 'dlh'
__date__ = '2018/1/2 14:50'

from django.conf.urls import url
# from django.views.generic import TemplateView

from .views import LoginView, IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(template_name="manage/index.html"), name='index'),
    url(r'^login', LoginView.as_view(template_name="manage/login.html"), name='login'),
]
