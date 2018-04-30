from django.shortcuts import render, redirect
from .forms import ThemeForm
from images.models import Image, Theme
# Create your views here.
def index(request):
    return render(request, 'offline/index.html', {'form': ThemeForm(initial={'theme': Theme.objects.get(name="Theme")})})

def game(request):
    if request.method == 'POST':
        form = ThemeForm(request.POST)
        theme = int(request.POST['theme'])
        images_qs = Image.objects.filter(theme=theme)
        images = []
        for i in images_qs:
            images.append(i.image.url)
        cover = Image.objects.filter(theme=Theme.objects.get(name='Covers').id)
        for j in cover:
            if j.image.name == 'images/{}.PNG'.format(Theme.objects.get(pk=theme).name):
                cover = j.image.url
                break
        return render(request, 'offline/game.html', {
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
        })
    else:
        return redirect('/offline-beta/')