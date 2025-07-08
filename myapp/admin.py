from django.contrib import admin
from .models import Video
from django.utils.html import format_html
class Videoadmin(admin.ModelAdmin):
    list_display = ('title','display_video')

    def display_video(self,obj):
        return format_html('<video width="300" height="300" controls><source src="{}"><video/>',obj.videofile.url)
admin.site.register(Video,Videoadmin)
