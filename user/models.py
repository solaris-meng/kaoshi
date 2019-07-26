from django.db import models

# Create your models here.
class User(models.Model):
    erp_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=20, verbose_name='真实姓名')
    nick_name = models.CharField(max_length=20, verbose_name='微信昵称')
    tel = models.CharField(max_length=32, verbose_name='手机号')

    openid_xcx = models.CharField(max_length=256, verbose_name='小程序ID')

    is_valid = models.BooleanField(default=True, verbose_name='有效')

    new_created = models.DateTimeField(null=True, auto_now_add=True)
    last_modified = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        verbose_name = '考试人员'
        verbose_name_plural = '考试人员' 

    def __str__(self):
        return self.name
