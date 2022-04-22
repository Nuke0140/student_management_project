from distutils.command.upload import upload
import profile
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    USER =(
        (1,'HOD'),
        (2,'STAFF'),
        (3,'STUDENT'),

        
    )



    user_type=models.CharField(choices=USER,max_length=58,default=1)

    profile.pic=models.ImageField(upload_to='media/profile_pic')