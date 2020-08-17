from rest_framework.viewsets import ModelViewSet
from bungalow.properties.api.serializers import PropertySerializer
from bungalow.properties.models import Property


class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
