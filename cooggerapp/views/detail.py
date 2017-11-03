from django.http import *
from django.shortcuts import render
from django.contrib.auth import *
from django.contrib import messages
from django.contrib.auth.models import User
from cooggerapp.models import Blog,Blogviews,OtherInformationOfUsers,UserFollow,Voters,Comment
from cooggerapp.views.tools import Topics,get_ip
from django.db.models import F
from django.contrib.auth.models import User
from bs4 import BeautifulSoup
from django.utils.text import slugify
import json
import os
from django.utils import timezone

def main_detail(request,blog_path,utopic,path):
    "blogların detail kısmı "
    queryset = Blog.objects.filter(url = blog_path)[0]
    username_id = queryset.username_id
    user = User.objects.filter(id = username_id)[0]
    ip = get_ip(request)
    nav_category = [nav for nav in nav_category_for_detail(username_id,utopic)]
    try:
        Blogviews.objects.filter(blog = queryset,ip = ip)[0].ip
    except:
        Blogviews(content = queryset,ip = ip).save()
        queryset.views = F("views") + 1
        queryset.save()
        queryset = Blog.objects.filter(url = blog_path)[0]
    try:
        stars = str(int(queryset.stars/queryset.hmstars))
    except ZeroDivisionError:
        stars = ""
    facebook = get_facebook(user)
    try:
        img_pp = get_head_img_pp(user)
    except:
        img_pp = ["/static/media/profil.png",None]
    elastic_search = dict(
        title = queryset.title+" | coogger",
        keywords = queryset.tag +","+user.username+" "+utopic+", "+utopic+",coogger "+queryset.category+", "+queryset.title,
        description = queryset.show,
        author = facebook,
        img = img_pp[0],
    )
    output = dict(
        detail = queryset,
        elastic_search = elastic_search,
        general = True,
        pp = img_pp[1],
        img = img_pp[0],
        stars = stars,
        nameoftopic = queryset.title,
        nav_category = nav_category,
        nameoflist = utopic,
        ogurl = request.META["PATH_INFO"],
        global_hashtag = [i for i in queryset.tag.split(",") if i != ""],
        comment_form = Comment.objects.filter(content=queryset),
    )
    return render(request,"detail/main_detail.html",output)

def stars(request,post_id,stars_id):
    if not request.is_ajax():
        return None
    user = User.objects.filter(username = request.user.username)
    request_username = request.user.username
    blog = Blog.objects.filter(id = post_id)[0]
    if not user.exists():
        return HttpResponse("Oy vermek için giriş yapmalı veya üye olmalısınız")
    user = user[0]
    try:
        vot = Voters.objects.filter(user = user,blog = blog) # daha önceden verdiği oy varsa alıyoruz
        old = vot[0].star
        vot.update(star = stars_id)
        blog.stars = F("stars")-old+stars_id
        blog.save()
    except IndexError: # ilk kez oylama yapıyor
        Voters(user = user,blog = blog,star = stars_id).save()
        blog.hmstars = F("hmstars")+1
        blog.stars = F("stars")+stars_id
        blog.save()
    first_li = """<li class="d-starts-li" data-starts-id="{{i}}" data-post-id="""+ post_id+ """>
            <img class="d-starts-a" src="/static/media/icons/star.svg">
            </li>"""
    second_li="""<li class="d-starts-li" data-starts-id="{{i}}" data-post-id="""+ post_id+ """>
                <img class="d-starts-a" src="/static/media/icons/star({{i}}).svg">
            </li>"""
    output = ""
    blog = Blog.objects.filter(id = post_id)[0]
    stars = blog.stars
    hmstars = blog.hmstars
    rate = stars/hmstars
    for i in range(0,10):
        if i <= int(rate):
            output += first_li.replace("{{i}}",str(i))
        if i > int(rate):
            output += second_li.replace("{{i}}",str(i))
        if i == 9:
            output +="<li> : "+str(hmstars)+"</li>"
    return HttpResponse(output)

def comment(request,content_path):
    if request.method=="POST" and request.is_ajax():
        comment = request.POST["comment"]
        content = Blog.objects.filter(url = content_path)[0]
        Comment(user=request.user,comment=comment,content = content).save()
        query = Blog.objects.filter(url = content_path)[0]
        query.hmanycomment = F("hmanycomment")+1
        query.save()
        return HttpResponse(
            json.dumps({
                "comment": comment,
                "user":request.user.username,
                "date":1,
            })
        )

def get_head_img_pp(user):
    pp = OtherInformationOfUsers.objects.filter(user = user)[0].pp
    if pp:
        img = "/media/users/pp/pp-"+user.username+".jpg"
    else:
        img = "/static/media/profil.png"
    return [img,pp]

def get_facebook(user):
    facebook = None
    try:
        for f in UserFollow.objects.filter(user = user):
            if f.choices  == "facebook":
                facebook = f.adress
    except:
        pass
    return facebook

def nav_category_for_detail(username_id,utopic):
    nav_category = Blog.objects.filter(username = username_id,content_list = utopic)
    for category in nav_category:
       yield category.url,category.title
