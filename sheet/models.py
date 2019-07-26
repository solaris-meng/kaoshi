from django.db import models

from shijuan.models import Shijuan

class Sheet(models.Model):
    erp_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=20, verbose_name='真实姓名')
    nick_name = models.CharField(max_length=20, verbose_name='微信昵称')
    tel = models.CharField(max_length=32, verbose_name='手机号')
    openid_xcx = models.CharField(max_length=256, verbose_name='小程序ID')

    is_valid = models.BooleanField(default=True, verbose_name='有效')

    shijuan = models.ForeignKey(Shijuan, on_delete=models.CASCADE, verbose_name='试卷', null=True)

    ctx = models.TextField(max_length=10000, verbose_name='原始记录')

    score_total = models.FloatField(default=0, verbose_name='满分')
    score = models.FloatField(default=0, verbose_name='得分')

    n_total = models.IntegerField(default=0, verbose_name='试题总数')
    n_correct = models.IntegerField(default=0, verbose_name='答对数量')
    n_incorrect = models.IntegerField(default=0, verbose_name='答错数量')

    new_created = models.DateTimeField(null=True, auto_now_add=True)
    last_modified = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        verbose_name = '答题卡'
        verbose_name_plural = '答题卡' 

    def __str__(self):
        return self.name

