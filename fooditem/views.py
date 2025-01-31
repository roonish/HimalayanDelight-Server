from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter,OrderingFilter
import logging
from .models import *
from .serializers import *

logger = logging.getLogger(__name__)

# Create your views here.
class FoodItemViewSet(ModelViewSet):
    logger.info('Calling all object from fooditem')
    queryset = FoodItem.objects.all()
    serializer_class=FoodItemSerializer
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['collection_id']
    search_fields = ['name','desc']
    ordering_fields = ['unit_price']

class FoodCollectionViewSet(ModelViewSet):
    queryset = FoodCollection.objects.all()
    serializer_class = FoodCollectionSerializer

class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class=CartItemSerializer

class FavouritesViewSet(ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class=FavouriteSerializer
    lookup_field = 'id'