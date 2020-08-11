from django.urls import path
import contest.views

urlpatterns = [
    path('', contest.views.home, name="home"),
]