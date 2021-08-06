from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Artist, Album, Song


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = "__all__"

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)

    def clean_name(self):
        artist_name = self.cleaned_data['name']
        if Artist.objects.filter(name__iexact=artist_name):
            raise ValidationError(f'{artist_name} already exists')
        return artist_name

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = "__all__"

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = "__all__"