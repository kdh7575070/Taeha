from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.utils import timezone
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

def createI(request):
    idea=Idea()
    idea.name=request.POST['name']
    idea.nuber=request.POST['number']
    idea.email=request.POST['email']

    idea.content=request.POST['content']
    try:
        idea.image = request.FILES['image']
    except:
        print('이미지가 없습니다')

    idea.manager=request.user
    idea.save()

    return render(request,'contestIdea.html', {'idea':idea})

#R
#홈페이지
def home(request):
    posts = Post.objects
    if posts.exists():
        random = random_post()
    else:
        random = None

    return render(request,'home.html',{'posts':posts, 'random_post':random})  

#공모전 게시글
def contestPost(request, post_id):
    post = get_object_or_404(Post,pk=post_id)
    user=request.user
    
    if post.likes.filter(id=user.id):
        state="Favorites_Registered"
    else:
        state="Favorites_Unregistered"

    comments = Comment.objects.all().filter(post = post)


    return render(request,'contestPost.html' ,{'post':post, 'state':state, 'comments':comments})

#공모전 개최자 페이지
def hostPage(request):
    return render(request,'hostPage.html')

#공모전 참여자 페이지
def participantPage(request):
    return render(request,'participantPage.html')

#게시글 등록 페이지
def createPost(request):
    return render(request, 'createPost.html')

#아이디어 등록 페이지
def createIdea(request):
    return render(request, 'createIdea.html')

#아이디어 게시글
def contestIdea(request):
    return render(request,'contestIdea.html')

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

def post_like(request, post_id):
    user = request.user # 로그인된 유저의 객체를 가져온다.
    post = get_object_or_404(Post, pk=post_id) # 좋아요 버튼을 누를 글을 가져온다.

    # 이미 좋아요를 눌렀다면 좋아요를 취소, 아직 안눌렀으면 좋아요를 누른다.
    if post.likes.filter(id=user.id): # 로그인한 user가 현재 post 객체에 좋아요를 눌렀다면
        post.likes.remove(user) # 해당 좋아요를 없앤다.
    else: # 아직 좋아요를 누르지 않았다면
        post.likes.add(user) # 좋아요를 추가한다.
    
    return redirect('/contestPost/'+str(post.id))

#댓글 관련
def comment_create(request, post_id):
    if request.method == "POST":
        comment=Comment()
        comment.body = request.POST['body']
        comment.c_writer = request.user
        comment.pub_date = timezone.datetime.now()
        comment.post = get_object_or_404(Post, pk=post_id)
        comment.save()

        return redirect('/contestPost/'+str(post_id))
    else:
        return redirect('/contestPost/'+str(post_id))

def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post_id = comment.post.id
    comment.delete()

    return redirect('/contestPost/'+str(post_id))