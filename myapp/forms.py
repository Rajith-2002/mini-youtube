from django import forms
from .models import Video, Shorts

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'


class ShortsForm(forms.ModelForm):
    class Meta:
        model = Shorts
        fields = '__all__'
