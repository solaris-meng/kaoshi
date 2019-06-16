from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='类别名')

    is_valid = models.BooleanField(default=True, verbose_name='有效')

    new_created = models.DateTimeField(null=True, auto_now_add=True)
    last_modified = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = '类别' 

    def __str__(self):
        return self.name

class Xuanzeti(models.Model):
    erp_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='类别', null=True)
    is_valid = models.BooleanField(default=True, verbose_name='有效')

    wenti = models.TextField(max_length=256, default='', verbose_name='问题')

    xuanxiang_a = models.TextField(max_length=256, default='', verbose_name='选项A')
    xuanxiang_b = models.TextField(max_length=256, default='', verbose_name='选项B')
    xuanxiang_c = models.TextField(max_length=256, default='', verbose_name='选项C')
    xuanxiang_d = models.TextField(max_length=256, default='', verbose_name='选项D')

    daan = models.CharField(max_length=6, default='a')

    new_created = models.DateTimeField(null=True, auto_now_add=True)
    last_modified = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        verbose_name = '单选题'
        verbose_name_plural = '单选题' 
    def __str__(self):
        return self.wenti
