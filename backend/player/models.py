from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

class Song(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='songs')
    name = models.CharField(max_length=100)
    song = models.FileField(upload_to='player/songs')
    song_thumbnail = models.ImageField('player/thumbnails', blank=True, null=True)

    crated_on = models.DateField(default=timezone.now)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(self.name)}_{self.id}'
        super(Song, self).save(*args, **kwargs)