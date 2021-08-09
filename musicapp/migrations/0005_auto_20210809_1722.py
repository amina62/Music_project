# Generated by Django 3.2.6 on 2021-08-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0004_auto_20210806_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='slug',
        ),
        migrations.AlterField(
            model_name='artist',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date of birth'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='first_name',
            field=models.CharField(max_length=250, null=True, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='last_name',
            field=models.CharField(max_length=250, null=True, verbose_name='Last Name'),
        ),
    ]
