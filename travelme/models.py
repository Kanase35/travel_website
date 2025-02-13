from django.db import models

# Create your models here.

class Destination(models.Model):
    # id = int
    name = models.CharField(max_length = 100)
    desc = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default = False)