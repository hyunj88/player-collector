from django.shortcuts import render
from .models import Player

# Create your views here.
players = [
    {'name': 'Kylian Mbappé', 'team': 'PSG', 'position': 'Forward', 'age': 24},
    {'name': 'Phil Foden ', 'team': 'Manchester City', 'position': 'Center Midfield', 'age': 22},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# index route for all players
def players_index(request):
    players = Player.objects.all()
    return render(request, 'players/index.html', { 'players': players })

def players_detail(request, player_id):
    player = Player.objects.get(id=player_id)
    return render(request, 'players/detail.html', { 'player': player })