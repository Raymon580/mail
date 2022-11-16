from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    def __str__(self):
        return self.username


class Email(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="emails")
    sender = models.ForeignKey(User, on_delete=models.PROTECT, related_name="sent")
    recipients = models.ManyToManyField("User", related_name="received")
    subject = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subject} by {self.sender}"