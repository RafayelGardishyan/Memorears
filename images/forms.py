from django import forms
from .models import Theme

class ThemeChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.name

class ImageForm(forms.Form):
    image = forms.FileField(label='Image', required=True)
    theme = ThemeChoiceField(queryset=Theme.objects.all(), label='Theme', required=True)

class ThemeForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255, required=True)
    description = forms.CharField(label='Description', max_length=1000, required=True)