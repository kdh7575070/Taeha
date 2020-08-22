from django.urls import path, include
import contest.views

urlpatterns = [
    path('', contest.views.home, name="home"),
    path('contestPost/<int:post_id>', contest.views.contestPost, name="contestPost"),
    path('hostPage/', contest.views.hostPage, name="hostPage"),
    path('participantPage/', contest.views.participantPage, name="participantPage"),
    path('createPost/', contest.views.createPost, name="createPost"),
    path('create/', contest.views.create, name="create"),
]

