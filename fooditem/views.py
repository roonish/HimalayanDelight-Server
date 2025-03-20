from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet,GenericViewSet,ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework import status
import logging
from .models import *
from .serializers import *

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Favourite
from .serializers import FavouriteSerializer

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
    serializer_class = FavouriteSerializer
    lookup_field = 'id'

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)  #  Return list of favourite items

    def create(self, request, *args, **kwargs):
        food_item_id = request.data.get("food_item")  # Extract food item ID

        if not food_item_id:
            return Response({"error": "food_item ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            food_item = FoodItem.objects.get(id=food_item_id)  # Fetch FoodItem
        except FoodItem.DoesNotExist:
            return Response({"error": "Food item not found"}, status=status.HTTP_404_NOT_FOUND)

        # Create the Favourite entry
        favourite = Favourite.objects.create(foodItem=food_item)
        serializer = self.get_serializer(favourite)

        return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return created objecT)


class RecommendationViewSet(ReadOnlyModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class=RecommendationSerializer