# Generated by Django 5.1.1 on 2024-09-28 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0014_alter_playlist_likes_alter_song_song_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
