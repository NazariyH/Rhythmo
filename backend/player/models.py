from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

class Song(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='songs')
    name = models.CharField(max_length=100)
    song = models.FileField(upload_to='player/songs')
    song_thumbnail = models.ImageField(upload_to='player/thumbnails', blank=True, null=True)

    created_on = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, blank=True)
    likes = models.ManyToManyField(User, related_name='song_is_liked_by', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(self.name)}_{self.id}'
        super(Song, self).save(*args, **kwargs)

class Playlist(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    created_on = models.DateTimeField(default=timezone.now)

    song = models.ManyToManyField(Song, related_name='songs', blank=True, null=True)
    playlist_thumbnail = models.ImageField(upload_to='player/playlist/thumbnails', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='playlist_is_liked_by', blank=True, null=True)

    def __str__(self):
        return self.title
