# Generated by Django 5.1.1 on 2024-09-27 10:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0010_alter_playlist_playlist_thumbnail'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='playlist_is_liked_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='song',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='song_is_liked_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
