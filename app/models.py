from django.db import models

# Create your models here.

class IceCreamShop(models.Model):
    shopname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.shopname} - {self.address}'

class IceCream(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    shop = models.ManyToManyField(IceCreamShop)
    
    def __str__(self):
        return f'{self.name} - {self.price}'

    
    