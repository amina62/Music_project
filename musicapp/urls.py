from django.urls import path
from . import views

urlpatterns = [

    #class based views urls:
    path('', views.ArtistListView.as_view(), name='artist-list'),
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
]