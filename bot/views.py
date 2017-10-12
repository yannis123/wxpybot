# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core import serializers
from bot import models
from wxpy import *
import PIL.Image

import os
import io

global bot,tuling

def logincallback(request):
    pass

def qrcallback(uuid,status,qrcode):
    #image = PIL.Image.open(io.BytesIO(qrcode))
    #print(image)
    #image.save(os.path.join(os.getcwd()+'/static/images/','q.jpg'))
    return HttpResponseRedirect('/bot/ref')

avatarpath='/static/images/avatar/'
list=list()


# Create your views here.
def index(request):
    bot=Bot(cache_path=True)
    bot.enable_puid('wxpy_puid.pkl')

    models.Friend.objects.all().delete()

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
    #bot = Bot(cache_path=True)
    result=models.Friend.objects.all()

    return render(request, 'home.html', {'friends':result,'qr':'/static/images/q.jpg'})

def search(request,puid,type):
    friend=models.Friend.objects.filter(puid=puid).first()

    if friend:
        if type==1:
            friend = ensure_one(bot.friends().search(friend.name))
        if type==2:
            friend=ensure_one(bot.groups().search(friend.name))

        if list.count(friend)==0:
            list.append(friend)
        else:
            list.remove(friend)

    return HttpResponse(serializers.serialize("json", list))

def delete(request):
    models.Friend.objects.all().delete()
    return HttpResponse("ok")

def login(request):
    bot = Bot(cache_path=False,qr_path=os.path.join(os.getcwd() + '/static/images/', 'q.jpg'))
    tuling = Tuling(api_key='77dc8a7f0488467eac0a4345655dcadd')
    #qrcallback(request)
    return render(request, 'login.html', {'friends':''})

def ref(request):
    return render(request, 'login.html', {'friends':''})


#@bot.register(list)
def reply_my_friend(msg):
    print(msg)
    #tuling.do_reply(msg)

#@bot.register()
def print_others(msg):
    for friend in list:
        if friend.name==msg.sender.name:
            print(msg.type)
            if msg.type=='Picture':
                msg.reply_msg('发图的是猪。。。')
            tuling.do_reply(msg)
            break

