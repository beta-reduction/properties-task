from rest_framework.fields import DateField
from rest_framework.serializers import ModelSerializer

from bungalow.properties.api.fields import ShortenedPrice
from bungalow.properties.models import Property


class PropertySerializer(ModelSerializer):
    price = ShortenedPrice()
    last_sold_date = DateField(format='%m/%d/%Y', allow_null=True, required=False)
    rentzestimate_last_updated = DateField(format='%m/%d/%Y', allow_null=True, required=False)
    zestimate_last_updated = DateField(format='%m/%d/%Y', allow_null=True, required=False)

    class Meta:
        model = Property

        fields = '__all__'

