from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    photo = models.ImageField(blank=True, upload_to="static/user_photo")

    def __str__(self):
        return self.user.username

    def is_adult(self):
        return self.age >= 18
