from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    album_title = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.album_title}_{self.artist}'

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    song_title = models.CharField(max_length=250)

    def __str__(self):
        return self.song_title

