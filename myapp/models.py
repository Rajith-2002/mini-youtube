from django.db import models

class Video(models.Model):
    title=models.CharField(max_length=50)
    videofile=models.FileField(upload_to='videos/')
    description=models.TextField()
    uploaded_at=models.DateTimeField(auto_now_add=True)


class Shorts(models.Model):
    title=models.CharField(max_length=100)
    short_file = models.FileField(upload_to='shorts/')
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
