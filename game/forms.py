from django import forms
from images.models import Theme

class ThemeChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.name

class GameForm(forms.Form):
    CHOICES = [('1 Spieler', '1 Spieler'), ('2 Spieler', '2 Spieler')]
    player_mode = forms.ChoiceField(label='Mode', widget=forms.RadioSelect, choices=CHOICES, required=True)
    theme = ThemeChoiceField(Theme.objects.all(), label='Theme', required=True)
