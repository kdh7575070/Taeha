# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=225)
    content =models.TextField()
    image=models.ImageField(upload_to='images/')

    start_time=models.DateTimeField()
    end_time=models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)# 해당 레코드 생성시 현재 시간 자동저장
    updated_at = models.DateTimeField(auto_now=True)# 해당 레코드 갱신시 현재 시간 자동저장

    category=models.CharField(max_length=225) #분야
    application_target=models.CharField(max_length=225) #응모 대상
    organizer=models.CharField(max_length=225) #주최기관
    prize_content =models.CharField(max_length=225) #시상내용

    prize_type =models.CharField(max_length=225)#경품 종류
    application_form=models.CharField(max_length=225) #응모 형태

    manager=models.ForeignKey(User, on_delete=models.CASCADE, null=True)#담당자 정보
    
    likes =models.ManyToManyField(
        User, # User 모델과 Shop 모델을 M : N 관계로 두겠다.
        through='Like', # Like라는 중개 모델을 통해 M : N 관계를 맺는다.
        through_fields=('post', 'user'), # Like에 shop 속성, user 속성을 추가하겠다.
        related_name='likes' # 1 : N  관계에서 market과 연결된 comment를 가져올 때 comment_set으로 가져왔는데, 
                            # related_name을 설정하면 shop.like_set이 아니라 shop.likes로 shop과 연결된 like를 가져올 수 있다.
        )

    def __str__(self):
        return self.name

    # 몇 개의 like와 연결되어 있는가를 보여준다.
    def like_count(self):
        return self.likes.count()

class Like(models.Model):
    # Post의 through_fields와 순서가 같아야 한다.
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True) # 특정 post가 삭제되면, 그 post의 즐겨찾기 정보 제거
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)