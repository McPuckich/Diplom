from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=250, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile/', default='profile/user-default.png')
    data_create = models.DateTimeField(auto_now_add=True)
    prof = models.CharField(max_length=200, null=True, blank=True)
    prof_info = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name
