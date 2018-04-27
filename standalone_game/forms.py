from django import forms
from images.models import Theme

class ThemeChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.name

class ThemeForm(forms.Form):
    theme = ThemeChoiceField(Theme.objects.all(), label='Theme', required=True)