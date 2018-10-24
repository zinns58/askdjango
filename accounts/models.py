from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)  # BAD CASE
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # GOOD CASE
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)