from django.db import models

# Create your models here.
class Book(models.Model):
    bk_name = models.CharField(max_length=100)
    bk_number = models.IntegerField()
