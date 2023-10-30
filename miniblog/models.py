from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class Blogdata(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    writeblog=models.TextField(max_length=200)
    authornm=models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.authornm

class UserProfile(models.Model):
   user = models.OneToOneField(User,on_delete=models.CASCADE)
   is_author = models.BooleanField(default=True)
   def __str__(self) -> str:
      return self.user.username