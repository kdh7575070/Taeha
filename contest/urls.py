from django.urls import path, include
import contest.views

urlpatterns = [
    path('', contest.views.home, name="home"),
    path('hostPage/', contest.views.hostPage, name="hostPage"),
    path('participantPage/', contest.views.participantPage, name="participantPage"),
    path('likedPage/', contest.views.likedPage, name="likedPage"),
    path('contestPost/createPost/', contest.views.createPost, name="createPost"),
    path('contestPost/create/', contest.views.create, name="create"),
    path('contestPost/<int:post_id>', contest.views.contestPost, name="contestPost"),
    path('contestPost/<int:post_id>/editPost/', contest.views.edit, name='editPost'),
    path('contestPost/<int:post_id>/update/', contest.views.update, name='update'),
    path('contestPost/<int:post_id>/delete/', contest.views.delete, name='delete'),
    path('contestPost/post_like/<int:post_id>', contest.views.post_like, name='post_like'),

    path('contestPost/<int:post_id>/createIdea/', contest.views.createIdea, name='createIdea'),
    path('contestPost/<int:post_id>/createI/', contest.views.createI, name='createI'),
    path('contestPost/<int:post_id>/deleteI/', contest.views.deleteI, name='deleteI'),
    path('contestPost/<int:post_id>/contestIdea/<int:idea_id>', contest.views.contestIdea, name='contestIdea'),
    
    path('search',contest.views.search, name='search'),
    path('comment_create/<int:post_id>',contest.views.comment_create, name='comment_create'),
    path('comment_delete/<int:post_id>',contest.views.comment_delete, name='comment_delete'),
]

