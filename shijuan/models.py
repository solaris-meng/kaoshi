from django.db import models

# Create your models here.
class Category(models.Model):
    erp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name='试卷类别名')

    is_valid = models.BooleanField(default=True, verbose_name='有效')

    new_created = models.DateTimeField(null=True, auto_now_add=True)
    last_modified = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        verbose_name = '试卷类别'
        verbose_name_plural = '试卷类别' 

    def __str__(self):
        return self.name

#
# 1. 定制选题
# 2. 随机抽题
# 3. 刷题模式
# 4. 试题乱序
# 5. 选项乱序
class Stype(models.Model):
    erp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name='考试方式')

    is_valid = models.BooleanField(default=True, verbose_name='有效')

    is_manual = models.BooleanField(default=False, verbose_name='手动选题')
    is_random = models.BooleanField(default=False, verbose_name='随机抽题')
    is_shiti_random = models.BooleanField(default=False, verbose_name='试题乱序')
    is_xuanxiang_random = models.BooleanField(default=False, verbose_name='选项乱序')

    total = models.IntegerField(default=0, verbose_name='试题数量')

    new_created = models.DateTimeField(null=True, auto_now_add=True)
    last_modified = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        verbose_name = '考试形式'
        verbose_name_plural = '考试形式' 

    def __str__(self):
        return self.name

class Shijuan(models.Model):
    erp_id = models.AutoField(primary_key=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='试卷类别', null=True)
    stype = models.ForeignKey(Stype, on_delete=models.CASCADE, verbose_name='考试形式', null=True)

    is_valid = models.BooleanField(default=True, verbose_name='有效')

    name = models.TextField(max_length=256, default='', verbose_name='试卷名称')
    shiti = models.TextField(max_length=2048, default='', verbose_name='试题号')

    new_created = models.DateTimeField(null=True, auto_now_add=True)
    last_modified = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        verbose_name = '试卷'
        verbose_name_plural = '试卷' 
    def __str__(self):
        return self.name
