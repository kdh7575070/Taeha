from django.urls import path, include
import contest.views

urlpatterns = [
    path('', contest.views.home, name="home"),
    path('hostPage/', contest.views.hostPage, name="hostPage"),
    path('participantPage/', contest.views.participantPage, name="participantPage"),
    path('contestPost/createPost/', contest.views.createPost, name="createPost"),
    path('contestPost/create/', contest.views.create, name="create"),
    path('contestPost/<int:post_id>', contest.views.contestPost, name="contestPost"),
    path('contestPost/editPost/<int:post_id>', contest.views.edit, name='editPost'),
    path('contestPost/update/<int:post_id>', contest.views.update, name='update'),
    path('contestPost/delete/<int:post_id>', contest.views.delete, name='delete'),
    path('contestPost/createIdea/<int:post_id>', contest.views.createIdea, name='createIdea'),
    path('contestPost/createI/<int:post_id>', contest.views.createI, name='createI'),
    # path('contestPost/deleteI/<int:post_id>', contest.views.createI, name='deleteI'),
    path('contestPost/<int:post_id>/contestIdea/<int:idea_id>', contest.views.contestIdea, name='contestIdea'),
    path('contestPost/post_like/<int:post_id>', contest.views.post_like, name='post_like'),
    path('search',contest.views.search, name='search'),
    path('comment_create/<int:post_id>',contest.views.comment_create, name='comment_create'),
    path('comment_delete/<int:post_id>',contest.views.comment_delete, name='comment_delete'),
]

