from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

import random

class Contact(models.Model):
    Username =models.CharField(max_length=100)
    UserEmail=models.CharField(max_length=200)
    Message=models.TextField()

    def __str__(self):
        return self.Username