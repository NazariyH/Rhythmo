from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Song
        fields = '__all__'