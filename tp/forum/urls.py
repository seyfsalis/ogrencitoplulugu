from django.urls import path
from . import views

urlpatterns = [
    path('liste/', views.liste, name = 'forum-liste'),
    path('forumekle/', views.forumEkle, name = 'forumEkle'),
    path('liste/forum/<int:id>', views.detail, name = 'detail'),
    path('yorum/<int:id>', views.yorumEkle, name = 'yorum'),


]