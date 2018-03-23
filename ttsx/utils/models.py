from django.db import models

class BaseModel(models.Model):
    update_date=models.DateField(auto_now=True,verbose_name='修改时间')
    add_date = models.DateField(auto_now_add=True,verbose_name='添加时间')
    isDelete = models.BooleanField(default=False,verbose_name='逻辑删除')
    class Meta:
        abstract=True   #表示类是模型基类，在数据库不创建表
