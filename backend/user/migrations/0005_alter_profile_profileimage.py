# Generated by Django 5.1.1 on 2024-09-23 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileImage',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
