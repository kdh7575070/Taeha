from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import *

# Create your views here.

#C

#R

#홈페이지
def home(request):
    return render(request,'home.html')

#공모전 게시글
def contestPost(request):
    return render(request,'contestPost.html')

#공모전 개최자 페이지
def hostPage(request):
    return render(request,'hostPage.html')

#공모전 참여자 페이지
def participantPage(request):
    return render(request,'participantPage.html')
#U

#D
