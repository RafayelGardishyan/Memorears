import sys

import os
from django.shortcuts import render, redirect
from .models import Image, Theme
from .forms import ImageForm, ThemeForm

# Create your views here.
def index(request):
    return render(request, 'settings_index.html', {})

def themes_index(request):
    themes = Theme.objects.all().order_by('name')
    return render(request, 'themes_index.html', {'themes': themes})

def themes_add(request):
    if not request.method == "POST":
        form = ThemeForm()
        return render(request, 'themes_add.html', {'form': form})
    else:
        form = ThemeForm(request.POST)
        if form.is_valid():
            i = Theme()
            i.name = form.cleaned_data['name']
            i.description = form.cleaned_data['description']
            i.save()
            return redirect('/settings/themes')
        else:
            return render(request, 'themes_add.html', {'form': form})

def themes_delete(request, id):
    theme = Theme.objects.get(pk=id)
    theme.delete()
    return redirect('/settings/themes')

def images_index(request):
    images = Image.objects.all().order_by('theme')
    return render(request, 'images_index.html', {'images': images})

def images_add(request):
    if not request.method == "POST":
        form = ImageForm()
        return render(request, 'images_add.html', {'form': form})
    else:
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            i = Image()
            i.image = form.cleaned_data['image']
            i.theme = form.cleaned_data['theme']
            i.save()
            return redirect('/settings/images')
        else:
            return render(request, 'images_add.html', {'form': form})

def images_delete(request, id):
    image = Image.objects.get(pk=id)
    if os.path.isfile(image.image.path):
        os.remove(image.image.path)
    image.delete()
    return redirect('/settings/images')
