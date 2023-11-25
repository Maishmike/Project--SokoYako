from django.db import models
from django.contrib.auth.models import User


class ContactCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=60)

    def __str__(self):
        return f"Contact Card for {self.user.username}"

