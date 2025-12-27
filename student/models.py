from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

User._meta.get_field('email')._unique = True