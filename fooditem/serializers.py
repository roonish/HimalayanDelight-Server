from rest_framework import serializers
from .models import FoodCollection,FoodItem,Favourite, CartItem

class FoodCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCollection
        fields=['title']

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields= ['id','name','desc','calory','unit_price','rating','collection','img']

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['foodItem','quantity']

class FavouriteSerializer(serializers.ModelSerializer):
     foodItem = FoodItemSerializer()
     class Meta:
            model = Favourite
            fields = ['id','foodItem']