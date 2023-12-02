from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add additional fields as needed for the profile
    # For example:
    # bio = models.TextField(blank=True)
    # profile_image = models.ImageField(upload_to='profile_images/', blank=True)
    # ...

    def __str__(self):
        return f"Profile for {self.user.username}"
