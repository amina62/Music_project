from django.db import models
# from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _
import datetime
# Create your models here.

class Artist(models.Model):
    first_name = models.CharField(max_length=250, null=True, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=250, null=True, verbose_name=_('Last Name'))
    date_of_birth = models.DateTimeField(blank=True, null=True, verbose_name=_('Date of birth'))
    nationality = models.CharField(max_length=250, null=True, verbose_name=_('Nationality'))

    def __str__(self):
        return self.first_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    album_title = models.CharField(max_length=250, verbose_name=_('Album Title'))

    def __str__(self):
        return f'{self.album_title}_{self.artist}'

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    song_title = models.CharField(max_length=250, verbose_name=_('Song Title'))

    def __str__(self):
        return self.song_title

