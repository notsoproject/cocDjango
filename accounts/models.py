from django.contrib.auth.models import AbstractUser
from django.db import models
from djongo import models as djongo_models
from bson import ObjectId
from .manager import UserManager


class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=100)
    # email = models.EmailField(max_length=255,verbose_name='Email address',unique=True)
    email = models.EmailField(max_length=255, verbose_name='Email address', unique=True, blank=False, null=False)
    playerTag = models.CharField(max_length=20, blank=False, null=False)
    # playerTag = models.CharField(max_length=20)
    # user_profile_image = models.ImageField(upload_to=profile)

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email
    
class Users_Details(models.Model):
    id = djongo_models.ObjectIdField()
    # user = models.CharField(max_length=24)  # Assuming user is referenced by a MongoDB ObjectId string
    # trophies = models.IntegerField()
    # Additional logic to handle user references or other complex structures


    def __str__(self):
        return f'{self.id} - Details'
