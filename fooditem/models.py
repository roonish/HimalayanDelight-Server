from django.db import models
from uuid import uuid4
from django.core.validators import MinValueValidator

class FoodCollection(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']

class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    calory = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=4,decimal_places=2)
    collection = models.ForeignKey(FoodCollection,on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class CartItem(models.Model):
    foodItem = models.ForeignKey(FoodItem,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(  
        validators=[MinValueValidator(1)])
