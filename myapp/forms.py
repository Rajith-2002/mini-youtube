from django import forms
from .models import Video,Shorts
class VideoUploadForm(forms.ModelForm):
    class Meta:
        model=Video
        fields='__all__'

import subprocess
import tempfile
from django import forms
from django.core.exceptions import ValidationError
from .models import Shorts

class ShortsForm(forms.ModelForm):
    class Meta:
        model = Shorts
        fields = '__all__'


