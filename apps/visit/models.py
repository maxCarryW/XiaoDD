from django.db import models
from base.models import BaseModel
from contact.models import Contact
from users.models import Area


# Create your models here.


class Visit(BaseModel):
    contact = models.ForeignKey(Contact, verbose_name='联络员')
    name = models.CharField(verbose_name='残疾人姓名', max_length=20)
    phone = models.CharField(verbose_name='残疾人电话', max_length=11)
    disabled_card = models.CharField(verbose_name='残疾证号', max_length=20, default='')
    area = models.ForeignKey(Area, verbose_name='所属地区')
    description = models.TextField(verbose_name='备注')
    checkState = models.IntegerField(verbose_name='残疾人信息审核状态', choices=((0, '未审核'), (1, '已通过'), (-1, '未通过')), default=0)
    checkDescription = models.TextField(verbose_name='残疾人审核信息')

    class Meta:
        verbose_name = '残疾人入户情况'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Picture(BaseModel):
    visit = models.ForeignKey(Visit, verbose_name='入户')
    path = models.ImageField(verbose_name='图片', max_length=100, upload_to="visit")

    class Meta:
        verbose_name = '图片信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.path
