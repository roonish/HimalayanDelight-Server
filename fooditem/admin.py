from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.FoodItem)
admin.site.register(models.CartItem)
admin.site.register(models.FoodCollection)

