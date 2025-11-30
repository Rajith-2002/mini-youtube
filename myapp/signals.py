from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Video, Shorts

@receiver(post_delete, sender=Video)
def delete_video_file(sender, instance, **kwargs):
    if instance.videofile:
        instance.videofile.delete(save=False)  # Cloudinary safe

@receiver(post_delete, sender=Shorts)
def delete_short_file(sender, instance, **kwargs):
    if instance.short_file:
        instance.short_file.delete(save=False)  # Cloudinary safe
