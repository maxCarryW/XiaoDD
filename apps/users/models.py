from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

from base.models import BaseModel


# Create your models here.

class UserProfile(AbstractUser):
    birthday = models.DateField(verbose_name=u'出生日期', null=True, blank=True)
    gender = models.CharField(verbose_name='性别', choices=(('male', u'男'), ('female', u'女')), max_length=6, default='male')
    phone = models.CharField(verbose_name='电话', max_length=11, null=True, blank=True)
    address = models.CharField(verbose_name='地址', max_length=100, default=u'')
    image = models.ImageField(verbose_name='头像', upload_to='user_logo', max_length=200, default='user_logo/default.png')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Area(models.Model):
    area_name = models.CharField(verbose_name='名称', max_length=50)
    ordering = models.IntegerField(verbose_name='序号')

    class Meta:
        verbose_name = '地区'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.area_name
