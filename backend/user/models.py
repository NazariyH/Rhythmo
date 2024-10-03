from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    GENDER = {
        'MALE': 'Male',
        "FEMALE": 'Female',
        'CISGENDER': 'Cisgender',
        'TRANSGENDER': 'Transgender',
        'NON-BINARY': 'Non-Binary',
        'INTERSEX': 'Intersex',
        'OTHERS': 'Others',
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    fullName = models.CharField(max_length=100, default='NoName')
    age = models.IntegerField(validators=[MaxValueValidator(150), MinValueValidator(13)], blank=True, null=True)
    bio = models.TextField(max_length=900, blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER, default='OTHERS')

    is_premium = models.BooleanField(default=False)

    followers = models.ManyToManyField(User, related_name='following', blank=True)
    profileImage = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.fullName:
            self.slug = f"{slugify(self.fullName)}_{self.user.id}"
        
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug
    

@receiver(pre_save, sender=Profile)
def update_slug(sender, instance, **kwargs):
    instance.slug = f"{slugify(instance.fullName)}_{instance.user.id}"