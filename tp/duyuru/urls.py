from django.urls import path
from . import views

urlpatterns = [
    path('liste/', views.listele, name='duyuru-liste')
]