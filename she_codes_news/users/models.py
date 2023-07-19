from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    pass
def __str__(self):
    return self.username

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.FileField(upload_to='profile_images')
    bio = models.TextField()
    def __str__(self):
        return self.user.username
