from rest_framework import serializers
from .models import FoodCollection,FoodItem,Favourite, CartItem, Recommendation

class FoodCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCollection
        fields=['title']

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields= ['id','name','desc','calory','unit_price','rating','collection','img']

class CartItemSerializer(serializers.ModelSerializer):
    foodItem = FoodItemSerializer(read_only=True)
    subTotal = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id','foodItem','quantity','subTotal']

    def get_subTotal(self,obj):
         return obj.quantity * obj.foodItem.unit_price

class FavouriteSerializer(serializers.ModelSerializer):
     foodItem = FoodItemSerializer()
     class Meta:
            model = Favourite
            fields = ['id','foodItem']

class RecommendationSerializer(serializers.ModelSerializer):
     foodItem = FoodItemSerializer()
     class Meta:
            model = Recommendation
            fields = ['id','foodItem']