import csv

from django.core.management.base import BaseCommand
from bungalow.properties.models import Property
from bungalow.properties.api.serializers import PropertySerializer

BULK_THRESHOLD = 100

class Command(BaseCommand):
    help = 'Insert entries of a csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        with open(options['csv_file'], 'r') as csv_file:
            csv_obj = csv.DictReader(csv_file)
            count = 0
            items = []
            for row in csv_obj:
                count += 1
                first_pass_clean = {k: v for k, v in row.items() if v != ''}
                serializer = PropertySerializer(data=first_pass_clean)
                if serializer.is_valid(raise_exception=True):
                    items.append(Property(**serializer.validated_data))

                if BULK_THRESHOLD <= count:
                    Property.objects.bulk_create(items)
                    items = []
