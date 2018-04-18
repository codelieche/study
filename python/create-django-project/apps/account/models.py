from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.


class UserProfile(AbstractUser):
    """
    自定义的用户Model
    拓展字段gender, nick_name, mobile, qq
    """

    GENDER_CHOICES = (
        ('male', "男"),
        ('female', "女"),
        ('secret', "保密")
    )

    nick_name = models.CharField(max_length=40, blank=True, verbose_name="昵称")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="secret",
                              verbose_name="性别")
    mobile = models.CharField(max_length=11, verbose_name="手机号", blank=True)
    qq = models.CharField(max_length=12, verbose_name="QQ号", blank=True)
    # 公司有时候会用到钉钉/微信发送消息，需要记录用户相关ID
    dingding = models.CharField(max_length=40, verbose_name="钉钉ID", blank=True, null=True)
    wechart = models.CharField(max_length=40, verbose_name="微信ID", blank=True, null=True)

    is_deleted = models.BooleanField(verbose_name="删除", default=False, blank=True)

    def __repr__(self):
        return "UserProfile:{}".format(self.username)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name


# 注意：get_user_model()方法可以获取到本系统使用的是哪个用户Model
# 默认的用户Model是：django.contrib.auth.models.User
# 在settings.py中配置：AUTH_USER_MODEL可以修改成指定的用户Model
# AUTH_USER_MODEL = "account.UserProfile"
User = get_user_model()
# 注意这句是要放在class UserProfile后面的
