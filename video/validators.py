from django.core.exceptions import ValidationError
from rpa.settings import BASE_DIR
from moviepy.editor import VideoFileClip
 
 

def file_size(value):
    # print (value)
    file_size=value.size
    if file_size>1000000000:
        raise ValidationError("maximum size is 1 GB")



def file_extension(value):
    name=value.name
    last = str(name.rsplit('.', 1)[-1])

    if last!="mp4"and"mkv":
        raise ValidationError("Invalid extension, only mp4 and mkv is allowed")