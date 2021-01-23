
from rest_framework import serializers
from .models import Episode

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['title', 'time', 'video']