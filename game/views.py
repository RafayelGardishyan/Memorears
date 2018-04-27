from django.shortcuts import render, redirect
from .forms import GameForm
from .models import Game
from images.models import Image, Theme
# Create your views here.
def index(request):
    form = GameForm()
    return render(request, 'game/index.html', {'form': form})

def settings(request):
    if request.method != 'POST':
        return redirect('/request')
    else:
        g = Game()
        g.mode = request.POST['player_mode']
        g.player1_score = 0
        g.player2_score = 0
        theme = request.POST['theme']
        x = 0
        g.save()
        for i in Image.objects.all().filter(theme=theme):
            if x < 6:
                g.card_image_sequence.add(i)
                x += 1
        g.save()
        request.session['mode'] = request.POST['player_mode']
        request.session['score1'] = 0
        request.session['score2'] = 0
        request.session['theme'] = request.POST['theme']
        return redirect('/request/screen/view')
