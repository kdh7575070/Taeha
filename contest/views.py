from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import *

import random

# Create your views here.

#C
def create(request):
    post=Post()
    post.title=request.POST['title']
    post.content=request.POST['content']
    try:
        post.image = request.FILES['image']
    except:
        print('이미지가 없습니다')

    #if( not post.image ):
        #print()

    post.start_date=request.POST['start_date']
    post.end_date=request.POST['end_date']

    post.category=request.POST.getlist('category[]')
    print(post.category)
    post.organizer=request.POST['organizer']
    post.total_prize=request.POST['total_prize']
    post.prize_type=request.POST['prize_type']

    post.manager=request.user
    post.save()

    return redirect('/contestPost/'+str(post.id))

#R
#홈페이지
def home(request):
    posts = Post.objects
    random = random_post()
    return render(request,'home.html',{'posts':posts, 'random_post':random})

#공모전 게시글
def contestPost(request, post_id):
    post = get_object_or_404(Post,pk=post_id)
    return render(request,'contestPost.html' ,{'post':post})

#공모전 개최자 페이지
def hostPage(request):
    return render(request,'hostPage.html')

#공모전 참여자 페이지
def participantPage(request):
    return render(request,'participantPage.html')

#게시글 등록 페이지
def createPost(request):
    return render(request, 'createPost.html')

#U
def edit(request, post_id):
    post=get_object_or_404(Post, pk=post_id) #특정 객체 가져오기 (없으면 404에러)
    return render(request, 'editPost.html', {'post':post})

def update(request, post_id):

    post=get_object_or_404(Post, pk=post_id) #특정 객체 가져오기 (없으면 404에러)
    post.title=request.POST['title']
    post.content=request.POST['content']
    try:
        post.image = request.FILES['image']
    except:
        print('이미지가 없습니다')

    #if( not post.image ):
        #print()

    post.start_date=request.POST['start_date']
    post.end_date=request.POST['end_date']

    post.category=request.POST.getlist('category[]')
    print(post.category)
    post.organizer=request.POST['organizer']
    post.total_prize=request.POST['total_prize']
    post.prize_type=request.POST['prize_type']

    post.manager=request.user
    post.save()

    return redirect('/contestPost/'+str(post.id))

#D

def delete(request, post_id):
    post=get_object_or_404(Post, pk=post_id) #특정 객체 가져오기 (없으면 404에러)
    post.delete()

    return redirect('home')

#
def search(request):
    post_list=Post.objects.all().order_by('-id')
    m=request.GET.get('post_name','init')

    if m:
        posts=post_list.filter(title__icontains=m)
    
    return render(request, 'search.html', {
        'posts':post_list,
        'post_search': posts,
        'm':m,
    })

def random_post():
    post_list=list(Post.objects.all())
    random.shuffle(post_list)
    return post_list[0]
