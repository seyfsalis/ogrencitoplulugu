from django.urls import path
from . import views

urlpatterns = [
    path('liste/', views.listele, name='duyuru-liste'),
    path('', views.index, name = 'index'),
    path('liste/duyuru/<int:id>', views.detail, name = 'detail'),
]