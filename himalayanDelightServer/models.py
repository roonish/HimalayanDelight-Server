from django.db import models
from uuid import uuid4
from django.core.validators import MinValueValidator

class FoodItem(models.model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    calory = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=4,decimal_places=2)




class CartItem(models.model):
    foodItem = models.ForeignKey(FoodItem,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(  
        validators=[MinValueValidator(1)])

    
