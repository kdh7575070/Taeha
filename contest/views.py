from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import *

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
    return render(request,'home.html',{'posts':posts})

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

#D
