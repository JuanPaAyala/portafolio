from django.db import models

# Create your models here.
class Transaction(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
