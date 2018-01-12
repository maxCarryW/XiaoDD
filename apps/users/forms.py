# !/user/bin/env python 
# -*- coding: utf-8 -*-
__author__ = 'dlh'
__date__ = '2018/1/4 16:00'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
