from django.contrib.auth.models import AbstractUser
from django.db import models
from djongo import models
from .manager import UserManager


class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=255,verbose_name='Email address',unique=True)
    playerTag = models.CharField(max_length=20)
    # user_profile_image = models.ImageField(upload_to=profile)

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email
    
class Users_Details(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='details')
    # name = models.CharField(max_length=255)
    trophies = models.DateField()


    def __str__(self):
        return f'{self.user.email} - Details'
