# !/user/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'dlh'
__date__ = '2018/1/2 14:50'

from django.conf.urls import url

from .views import LoginView, RegisterView, R_stateView, MyselfView, ForgetPasswordView

from .views import ContactListView, ContactCheckView, DeleteView

urlpatterns = [

    url(r'^myself', MyselfView.as_view(), name='myself'),
    url(r'^login', LoginView.as_view(), name='login'),
    url(r'^register', RegisterView.as_view(), name='register'),
    url(r'^r_state', R_stateView.as_view(), name='r_state'),
    url(r'^forget', ForgetPasswordView.as_view(), name='forget'),

    # 后台管理模块
    url(r'^list', ContactListView.as_view(template_name="manage/contact_list.html"), name='list'),
    url(r'^check', ContactCheckView.as_view(), name='check'),
    url(r'^delete/(?P<id>\d+)/', DeleteView.as_view(), name='delete'),
    url(r'^update/(?P<id>\d+)/', ContactCheckView.as_view(), name='update'),

]
