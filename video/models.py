from csv import field_size_limit
from pydoc import importfile
from django.db import models
from .validators import     file_extension,   file_size
from datetime import datetime, date
from django.core.validators import FileExtensionValidator

# Create your models here.

class Video(models.Model):
    caption = models.CharField(max_length=100)
    video=models.FileField(upload_to='uploads/video_files',validators=[file_size,file_extension ])
    created_time=models.DateField(auto_now_add=True)
    # thumbnail = models.FileField(upload_to='uploads/thumbnails', validators = [FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])

    def __str__(self):
        return self.caption
 
