from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import ArtistForm, AlbumForm, SongForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

# Create your views here.

from .models import Artist, Album, Song
from .forms import ArtistForm
#class based views:

# Artists
main_html = "list.html"


class ArtistListView(ListView):
    model = Artist
    template_name = main_html
    context_object_name = 'artists'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('Artists List')
        context['form'] = ArtistForm
        return context


class ArtistCreateView(CreateView):
    #model = Artist
    template_name = 'artist_create.html'
    # fields = "__all__"
    form_class = ArtistForm

    def form_valid(self, form):
        form.save()
        return JsonResponse(data={"message": 'All good'}, status=201)

    def form_invalid(self, form):
        return JsonResponse(data={"errors": form.errors}, status=500)


class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'artist_detail.html'
    context_object_name = 'artists'

class ArtistUpdateView(UpdateView):
    model = Artist
    # template_name = 'artist_update.html'
    context_object_name = 'artists'
    form_class = ArtistForm

    def get(self, request, *args, **kwargs):
        if artist := Artist.objects.get(pk=kwargs['pk']):
            return JsonResponse(data={
                "first_name": artist.first_name,
                "last_name": artist.last_name,
                "DOB": artist.date_of_birth,
                "nationality": artist.nationality
            })

    def form_valid(self, form):
        form.save()
        return JsonResponse({
            "message": "Artist updated",
            "url": self.get_success_url(),

            "first_name": form.cleaned_data['first_name'],
            "last_name": form.cleaned_data['last_name'],
            "DOB": form.cleaned_data['date_of_birth'],
            "nationality": form.cleaned_data['nationality']
        }, status=201)

    def form_invalid(self, form):
        return JsonResponse({'error': form.errors})

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