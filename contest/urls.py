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
    path('search',contest.views.search, name='search')
]

