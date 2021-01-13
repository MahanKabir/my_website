
from django import forms

from episode.models import Episode


class EpisodeForm(forms.ModelForm):
    class Meta:
        model = Episode
        fields = ['title', 'time', 'video']