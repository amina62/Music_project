# Generated by Django 3.2.6 on 2021-08-06 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_artist_nationality'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='name',
        ),
        migrations.AddField(
            model_name='artist',
            name='first_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='last_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_title',
            field=models.CharField(max_length=250, verbose_name='Album Title'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='nationality',
            field=models.CharField(max_length=250, null=True, verbose_name='Nationality'),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_title',
            field=models.CharField(max_length=250, verbose_name='Song Title'),
        ),
    ]