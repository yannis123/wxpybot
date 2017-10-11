# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from bot import models
from wxpy import *
import os

avatarpath='/static/images/avatar/'
list=[]
bot=Bot(cache_path=True)
tuling = Tuling(api_key='77dc8a7f0488467eac0a4345655dcadd')
# Create your views here.
def index(request):

    bot.enable_puid('wxpy_puid.pkl')

    myfriends=bot.friends()

    for friend in myfriends:
        #print(friend.puid)
        friend.get_avatar(os.path.join(os.getcwd()+avatarpath,str(friend.puid)+'.jpg'))
        model=models.Friend(type=1,puid=friend.puid,name=friend.name,nick_name=friend.nick_name,avatar=avatarpath+str(friend.puid)+'.jpg')
        model.save()


    for group in bot.groups():
        group.get_avatar(os.path.join(os.getcwd()+avatarpath,str(group.puid)+'.jpg'))
        model=models.Friend(type=2,puid=group.puid,name=group.name,nick_name=group.nick_name,avatar=avatarpath+str(group.puid)+'.jpg')
        model.save()
    # 使用图灵机器人自动与指定好友聊天
    return render(request, 'index.html', {'friends':myfriends})

def home(request):
    bot = Bot(cache_path=True)
    result=models.Friend.objects.all()
    friend = bot.groups().search('赌博')
    print(friend)
    list.append(friend)
    return render(request, 'home.html', {'friends':result})

def search(request,puid,type):
    friend=models.Friend.objects.filter(puid=puid)
    if friend:
        if type==1:
            friend = ensure_one(bot.friends().search(friend[0].name))
        if type==2:
            friend=ensure_one(bot.groups().search(friend[0].name))

        if list.count(friend)==0:
            list.append(friend)

    return render(request, 'search.html', {'friends':list})

@bot.register(list)
def reply_my_friend(msg):
    print(msg)
    tuling.do_reply(msg)
