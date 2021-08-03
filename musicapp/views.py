from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ArtistForm, AlbumForm, SongForm

# Create your views here.

from .models import *

def home(request):
    artists = Artist.objects.all()
    albums = Album.objects.all()
    songs = Song.objects.all()
    context = {'artists': artists, 'albums': albums, 'songs':songs}
    return render(request, 'home.html', context)

def create_artist(request):
    form = ArtistForm()
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'artist_form.html', context)

def update_artist(request, pk):
    artist = Artist.objects.get(id=pk)
    form = ArtistForm(instance=artist)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'artist_form.html', context)

def delete_artist(request, pk):
    artist = Artist.objects.get(id=pk)
    if request.method == 'POST':
        artist.delete()
        return redirect('/')

    context = {'item': artist}
    return render(request, 'artist_form.html', context)

# Albums:
def create_album(request):
    form = AlbumForm
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'album_form.html', context)

def update_album(request, pk):
    album = Album.objects.get(id=pk)
    form = AlbumForm(instance=album)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'album_form.html', context)

def delete_album(request, pk):
    album = Album.objects.get(id=pk)
    if request.method == 'POST':
        album.delete()
        return redirect('/')

    context = {'item': album}
    return render(request, 'album_form.html', context)

# Songs:
def create_song(request):
    form = SongForm
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'song_form.html', context)

def update_song(request, pk):
    song = Song.objects.get(id=pk)
    form = SongForm(instance=song)
    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'song_form.html', context)

def delete_song(request, pk):
    song = Song.objects.get(id=pk)
    if request.method == 'POST':
        song.delete()
        return redirect('/')

    context = {'item': song}
    return render(request, 'song_form.html', context)





