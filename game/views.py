from django.shortcuts import render, redirect
from .models import Game
from images.models import Image, Theme


def index(request):
    theme = int(request.session['theme'])
    images_qs = Image.objects.filter(theme=theme)
    images = []
    for i in images_qs:
        images.append(i.image.url)
    cover = Image.objects.filter(theme=Theme.objects.get(name='Covers').id)
    for j in cover:
        if j.image.name == 'images/{}.PNG'.format(Theme.objects.get(pk=theme).name) or j.image.name == 'images/{}.png'.format(Theme.objects.get(pk=theme).name):
            cover = j.image.url
            break
    gameid = request.session['game_id']
    return render(request, 'online/game.html', {
        'cover': cover,
        'image1': images[0],
        'image2': images[1],
        'image3': images[2],
        'image4': images[3],
        'image5': images[4],
        'image6': images[5],
        'image7': images[6],
        'image8': images[7],
        'image9': images[8],
        'image10': images[9],
        'image11': images[10],
        'image12': images[11],
        'gameid': gameid
    })


def create(request):
    g = Game()
    g.save()
    request.session['game_id'] = g.joinid
    return redirect('/lobby')


def lobby(request):
    return render(request, 'online/lobby.html', {'gameid': request.session['game_id']})


def playerscreen(request):
    return render(request, 'online/playerscreen.html', {})
