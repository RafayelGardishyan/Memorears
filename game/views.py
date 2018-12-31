import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Game
from images.models import Image, Theme


def change_turn(request, do):
    if do == 0:
        return JsonResponse([False], safe=False)
    g = Game.objects.get(joinid=int(request.session['game_id']))
    if g.turn == g.player_count:
        g.turn = 1
    else:
        g.turn += 1
    g.save()
    return JsonResponse([True], safe=False)


def index(request):
    theme = int(request.session['theme'])
    images_qs = Image.objects.filter(theme=theme)
    images = []
    for i in images_qs:
        images.append(i.image.url)
    cover = Image.objects.filter(theme=Theme.objects.get(name='Covers').id)
    for j in cover:
        if j.image.name == 'images/{}.PNG'.format(Theme.objects.get(pk=theme).name):
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


def setopencard(request, cardid, player):
    g = Game.objects.get(joinid=int(request.session['game_id']))
    if player == g.turn:
        if g.opencard1 == 25 or g.opencard1 == None:
            g.opencard1 = cardid
        elif g.opencard1 <= 25:
            g.opencard2 = cardid
    g.save()
    return JsonResponse([g.opencard1, g.opencard2], safe=False)


def reset(request):
    g = Game.objects.get(joinid=int(request.session['game_id']))
    g.opencard1, g.opencard2 = 25, 25
    g.save()
    return JsonResponse([True], safe=False)


def resetscore(request):
    g = Game.objects.get(joinid=int(request.session['game_id']))
    g.player_scores = json.dumps([0] * g.player_count)
    g.save()
    return JsonResponse([True], safe=False)


def setscore(request, player, plus):
    g = Game.objects.get(joinid=int(request.session['game_id']))
    if g.turn == player:
        scores = json.loads(g.player_scores)
        scores[player - 1] += plus
        g.player_scores = json.dumps(scores)
    g.save()
    return JsonResponse([g.player_scores, True], safe=False)


def create(request):
    g = Game()
    g.save()
    request.session['game_id'] = g.joinid
    return redirect('/lobby')


def lobby(request):
    return render(request, 'online/lobby.html', {'gameid': request.session['game_id']})


def get(request):
    g = Game.objects.get(joinid=int(request.session['game_id']))
    return JsonResponse({
        'joinid': g.joinid,
        'opencard1': g.opencard1,
        'opencard2': g.opencard2,
        'player_score': g.player_scores,
        'turn': g.turn
    }, safe=False)


def getwid(request, id):
    g = Game.objects.get(joinid=id)
    request.session['game_id'] = g.joinid
    return JsonResponse({
        'joinid': g.joinid,
        'opencard1': g.opencard1,
        'opencard2': g.opencard2,
        'player_score': g.player_scores,
        'turn': g.turn
    }, safe=False)


def playerscreen(request):
    return render(request, 'online/playerscreen.html', {})


def setonline(request, id):
    g = Game.objects.get(joinid=id)
    if g.locked:
        return JsonResponse([False], safe=False)
    g.player_count += 1
    g.player_scores = json.dumps([0] * g.player_count)
    print(g.player_scores)
    g.save()
    return JsonResponse([g.player_count], safe=False)


def lockroom(request):
    g = Game.objects.get(joinid=int(request.session['game_id']))
    if g.player_count == 0:
        return redirect("/lobby")
    g.locked = True
    g.save()
    return redirect("/online")
