from django.db import models

from base.models import BaseModel
from users.models import Area


# Create your models here.

class Contact(BaseModel):
    name = models.CharField(verbose_name='姓名', max_length=20)
    password = models.CharField(verbose_name='密码', max_length=11, default='123456')
    phone = models.CharField(verbose_name='电话', max_length=11)
    area = models.ForeignKey(Area, verbose_name='所属地区')
    openId = models.CharField(verbose_name='openId', max_length=50, null=True, blank=False)
    bindState = models.CharField(verbose_name='绑定状态', choices=(('未绑定', '未绑定'), ('已绑定', '已绑定')), max_length=6, default='未绑定')
    checkState = models.IntegerField(verbose_name='审核状态', choices=((0, '未审核'), (1, '已通过'), (-1, '未通过')), default=0)

    checkDescription = models.TextField(verbose_name='审核信息')

    class Meta:
        verbose_name = '联络员'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    @property
    def simple_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'area': self.area,
        }

    @property
    def area_name(self):
        return self.area and self.area.area_name or ''
