from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    UNCLASSIFIED = 0
    STANDARD = 1
    URGENT = 2
    CATEGORY_CHOICES = [
        (UNCLASSIFIED, 'Unclassified'),
        (STANDARD, 'Standard'),
        (URGENT, 'Urgent'),
    ]
    name = models.CharField(max_length=255)
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=UNCLASSIFIED)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
