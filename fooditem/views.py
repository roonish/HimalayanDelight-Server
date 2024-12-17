from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

# Create your views here.
class FoodItemViewSet(ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class=FoodItemSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields = ['collection_id']

class FoodCollectionViewSet(ModelViewSet):
    queryset = FoodCollection.objects.all()
    serializer_class = FoodCollectionSerializer

class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class=CartItemSerializer

class FavouritesViewSet(ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class=FavouriteSerializer