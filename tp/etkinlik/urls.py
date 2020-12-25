from django.urls import path
from . import views

urlpatterns = [
    path('liste/', views.liste, name = 'etkinlik'),
    path('liste/etkinlik/<int:id>', views.detail, name = 'detail'),
]