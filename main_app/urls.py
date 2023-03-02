from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('players/', views.players_index, name='index'),
    path('cats/<int:player_id>/', views.players_detail, name='detail'),
]