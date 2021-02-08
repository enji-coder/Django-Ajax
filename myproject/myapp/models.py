from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    contact=models.CharField(max_length=11)

class Product(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Brand(models.Model):
    pid= models.ForeignKey(Product, on_delete = models.CASCADE)
    brand_name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.brand_name