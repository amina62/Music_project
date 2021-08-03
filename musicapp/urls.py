from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
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