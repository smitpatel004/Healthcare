from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.tweet_home,name="tweet_home"),
    path('list/',views.tweet_list,name="tweet_list"),
    path('l/',views.Quiz_list,name="quiz_list"),
    path('c/',views.Quiz_create,name="qui_create"),
    path('create/',views.tweet_create,name="tweet_create"),
    path('<int:tweet_id>/edit',views.tweet_edit,name="tweet_edit"),
    path('<int:tweet_id>/delete',views.tweet_delete,name="tweet_delete")
    # path('tweet_list/',views.tweet_list,name="tweet_list")
]
