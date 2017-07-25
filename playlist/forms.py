from django import forms
from .models import PlayList

class PlayListForm(forms.ModelForm):
    class Meta:
        model = PlayList
        fields =('mal_or_kitsu_link', 'kitsu_or_mal','size', 'mode', 'order')