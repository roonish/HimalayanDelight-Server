from django.contrib import admin
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register('fooditems',FoodItemViewSet)
router.register('foodcollections',FoodCollectionViewSet)
router.register('cartitems',CartItemViewSet)
router.register('favourites',FavouritesViewSet)
router.register('recommendation',RecommendationViewSet)



urlpatterns = router.urls
