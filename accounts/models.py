from django.contrib.auth.models import AbstractUser
from django.db import models
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
    address = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    profile_image = models.ImageField(upload_to='profile_images', blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.email} - Details'
