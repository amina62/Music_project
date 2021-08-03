from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ArtistForm, AlbumForm, SongForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

from .models import *

#class based views:

# Artists
main_html = "list.html"

class ArtistListView(ListView):
    model = Artist
    template_name = main_html
    context_object_name = 'artists'

class ArtistCreateView(CreateView):
    model = Artist
    template_name = 'artist_create.html'
    # template_name = main_html
    fields = ['name', ]
    success_url = reverse_lazy('artist-list')

class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'artist_detail.html'
    context_object_name = 'artists'

class ArtistUpdateView(UpdateView):
    model = Artist
    template_name = 'artist_update.html'
    context_object_name = 'artists'
    fields = ['name', ]
    def get_success_url(self):
        return reverse_lazy('artist-detail', kwargs={'pk': self.object.id})

class ArtistDeleteView(DeleteView):
    model = Artist
    template_name = 'artist_delete.html'
    success_url = reverse_lazy('artist-list')

# Albums
class AlbumListView(ListView):
    model = Album
    template_name = 'album_list.html'
    context_object_name = 'albums'

class AlbumCreateView(CreateView):
    model = Album
    template_name = 'album_create.html'
    fields = '__all__'
    success_url = reverse_lazy('album-list')

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'album_detail.html'
    context_object_name = 'albums'

class AlbumUpdateView(UpdateView):
    model = Album
    template_name = 'album_update.html'
    context_object_name = 'albums'
    fields = '__all__'
    def get_success_url(self):
        return reverse_lazy('album-detail', kwargs={'pk': self.object.id})

class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'album_delete.html'
    success_url = reverse_lazy('album-list')


# Songs
class SongsListView(ListView):
    model = Song
    template_name = 'song_list.html'
    context_object_name = 'songs'

class SongCreateView(CreateView):
    model = Song
    template_name = 'song_create.html'
    fields = '__all__'
    success_url = reverse_lazy('song-list')

class SongDetailView(DetailView):
    model = Song
    template_name = 'song_detail.html'
    context_object_name = 'songs'

class SongUpdateView(UpdateView):
    model = Song
    template_name = 'song_update.html'
    context_object_name = 'songs'
    fields = '__all__'
    def get_success_url(self):
        return reverse_lazy('song-detail', kwargs={'pk': self.object.id})

class SongDeleteView(DeleteView):
    model = Song
    template_name = 'song_delete.html'
    success_url = reverse_lazy('song-list')


#function based views:
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





