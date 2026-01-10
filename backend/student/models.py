# student/models.py
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=30, unique=True)

    def __str__(self):
        # Improved: fallback to username or email if names are empty
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name}"
        elif self.user.first_name:
            return self.user.first_name
        elif self.user.email:
            return self.user.email
        else:
            return self.user.username  # fallback to username