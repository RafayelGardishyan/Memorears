from django import forms
from images.models import Theme

class ThemeChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.name

class ThemeForm(forms.Form):
    theme = ThemeChoiceField(Theme.objects.all().exclude(name='Covers').exclude(name='SiteAssets'), label='', required=True)
    CHOICES = [('1', 'Single Player'),
               ('2', 'Multi Player')]
    mode = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), label='')
