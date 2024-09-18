from django.db import models

# Create your models here.

class Products(models.Model):
    
    name = models.CharField(unique=True, max_length= 100)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    image = models.ImageField()
    def __str__(self):
        return self.name