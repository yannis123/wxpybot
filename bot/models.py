# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Friend(models.Model):
    puid=models.CharField(max_length = 100)  #wxpy 特有的聊天对象/用户ID
    name=models.CharField(max_length = 20)  #聊天对象好友名
    nick_name=models.CharField(max_length=50)   #该聊天对象的昵称 (好友、群员的昵称，或群名称)
    avatar=models.CharField(max_length= 200 )   #头像
    date_time = models.DateTimeField(auto_now_add=True)  # 更新日期

