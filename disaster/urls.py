from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'states', StateViewSet)
router.register(r'villages', VillageViewSet)
router.register(r'predictions', DisasterPredictionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]