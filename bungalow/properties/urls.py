from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bungalow.properties.api.viewsets import PropertyViewSet

router = DefaultRouter()
router.register('', PropertyViewSet, basename='property')

urlpatterns = [
    path('', include(router.urls))
]