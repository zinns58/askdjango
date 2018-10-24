from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # todo : BAD CASE
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)