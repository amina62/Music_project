from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    #class based views urls:
    path('artist/', views.ArtistListView.as_view(), name='artist-list'),
    path('artist-create/', views.ArtistCreateView.as_view(), name='artist-create'),
    path('artist/<int:pk>', views.ArtistDetailView.as_view(), name='artist-detail'),
    path('artist/update/<int:pk>', views.ArtistUpdateView.as_view(), name='artist-update'),
    path('artist/delete/<int:pk>', views.ArtistDeleteView.as_view(), name='artist-delete'),

    path('album/', views.AlbumListView.as_view(), name='album-list'),
    path('album-create/', views.AlbumCreateView.as_view(), name='album-create'),
    path('album/<int:pk>', views.AlbumDetailView.as_view(), name='album-detail'),
    path('album/update/<int:pk>', views.AlbumUpdateView.as_view(), name='album-update'),
    path('album/delete/<int:pk>', views.AlbumDeleteView.as_view(), name='album-delete'),

    path('song/', views.SongsListView.as_view(), name='song-list'),
    path('song-create/', views.SongCreateView.as_view(), name='song-create'),
    path('song/<int:pk>', views.SongDetailView.as_view(), name='song-detail'),
    path('song/update/<int:pk>', views.SongUpdateView.as_view(), name='song-update'),
    path('song/delete/<int:pk>', views.SongDeleteView.as_view(), name='song-delete'),

    #functial based views urls:
    path('add_artist/', views.create_artist, name='create-artist'),
    path('update_artist/<str:pk>', views.update_artist, name='update-artist'),
    path('delete_artist/<str:pk>', views.delete_artist, name='delete-artist'),

    path('add_album/', views.create_album, name='create-album'),
    path('update_album/<str:pk>', views.update_album, name='update-album'),
    path('delete_album/<str:pk>', views.delete_album, name='delete-album'),

    path('add_song/', views.create_song, name='create-song'),
    path('update_song/<str:pk>', views.update_song, name='update-song'),
    path('delete_song/<str:pk>', views.delete_song, name='delete-song'),
]