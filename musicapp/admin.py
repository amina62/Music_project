from django.contrib import admin

# Register your models here.

from .models import Artist, Album, Song

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
