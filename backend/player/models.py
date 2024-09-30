from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

class Song(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='songs')
    name = models.CharField(max_length=100)
    song = models.FileField(upload_to='player/songs')
    song_thumbnail = models.ImageField(upload_to='player/thumbnails', blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='song_is_liked_by', blank=True)

    def __str__(self):
        return self.name


class Playlist(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    title = models.CharField(unique=True, max_length=100)
    description = models.CharField(max_length=250, blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    song = models.ManyToManyField(Song, related_name='songs', blank=True)
    playlist_thumbnail = models.ImageField(upload_to='player/playlist/thumbnails', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='playlist_is_liked_by', blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Song)
def create_song_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)


@receiver(pre_save, sender=Playlist)
def create_playlist_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
