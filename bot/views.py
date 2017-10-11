# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from wxpy import *
from django.shortcuts import render
from django.http import HttpResponse
from bot.models import Friend
import os

list=[]
bot=Bot(cache_path=True)
# Create your views here.
def index(request):

    bot.enable_puid('wxpy_puid.pkl')

    myfriends=bot.friends()

    for friend in myfriends:
        #print(friend.puid)
        friend.get_avatar(os.path.join(os.getcwd()+'\\static\\images\\avatar\\',str(friend.puid)+'.jpg'))
        model=Friend(puid=friend.puid,name=friend.name,nick_name=friend.nick_name,avatar='\\static\\images\\avatar\\'+str(friend.puid)+'.jpg')
        model.save()


    for group in bot.groups():
        group.get_avatar(os.path.join(os.getcwd()+'\\static\\images\\avatar\\',str(group.puid)+'.jpg'))
        model=Friend(puid=group.puid,name=group.name,nick_name=group.nick_name,avatar='\\static\\images\\avatar\\'+str(group.puid)+'.jpg')
        model.save()
        if group.name=='赌神':
            list.append(group)
    # 使用图灵机器人自动与指定好友聊天

    return render(request, 'index.html', {'friends':myfriends})

def home(request):
    result=Friend.objects.all()
    return render(request, 'home.html', {'friends':result})


@bot.register(list)
def reply_my_friend(msg):
    print(msg)
    tuling.do_reply(msg)
