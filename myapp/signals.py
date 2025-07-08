import os
import time
import gc
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Video, Shorts  # Replace with your actual model names

@receiver(post_delete, sender=Video)
def delete_video_file(sender, instance, **kwargs):
    file_path = instance.videofile.path
    try:
        gc.collect()         # Free memory
        time.sleep(0.5)      # Wait for file release (important for Windows)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print("Video file deleted:", file_path)
    except Exception as e:
        print("Error deleting video file:", e)

@receiver(post_delete, sender=Shorts)
def delete_short_file(sender, instance, **kwargs):
    file_path = instance.short_file.path
    try:
        gc.collect()
        time.sleep(0.5)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print("Short file deleted:", file_path)
    except Exception as e:
        print("Error deleting short file:", e)
