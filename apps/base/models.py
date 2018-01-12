from django.db import models

from datetime import datetime


# Create your models here.

class BaseModel(models.Model):
    create_time = models.DateTimeField(verbose_name="创建时间", default=datetime.now)
    update_time = models.DateTimeField(verbose_name="更新时间", null=True, blank=True, default=None)
    delete_time = models.DateTimeField(verbose_name="删除时间", null=True, blank=True, default=None)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.id and not self.delete_time:
            self.update_time = datetime.now()
        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def delete(self, using=None, keep_parents=False):
        self.delete_time = datetime.now()
        self.save()
