from datetime import date
from decimal import Decimal

from django.test import TestCase

from bungalow.properties.models import Property, AreaUnit, HomeType


class PropertyAPITest(TestCase):
    api_endpoint = '/api/properties/'

    def post(self, data):
        return self.client.post(self.api_endpoint, data, format='json')

    def put(self, obj_id, data):
        return self.client.put(f'{self.api_endpoint}{obj_id}/', data, format='json')

    def get(self, obj_id):
        return self.client.get(f'{self.api_endpoint}{obj_id}/')

    def get_all(self):
        return self.client.get(self.api_endpoint)

    def delete(self, obj_id):
        return self.client.delete(f'{self.api_endpoint}{obj_id}/')

    def test_retrieve(self):
        prop_data = {
            'area_unit': AreaUnit.AREA_UNIT_SQFT,
            'home_type': HomeType.HOME_TYPE_SINGLE_FAMILY,
            'bathrooms': Decimal('2.5'),
            'bedrooms': 4,
            'home_size': 4000,
            'property_size': 8000,
            'link': 'http://google.com',
            'last_sold_date': date(day=25, month=3, year=2017),
            'last_sold_price': Decimal('250000'),
            'price': Decimal('250000'),
            'rent_price': None,
            'rentzestimate_amount': Decimal('1000'),
            'rentzestimate_last_updated': date(day=25, month=3, year=2020),
            'tax_value': Decimal('250000'),
            'tax_year': 2019,
            'year_built': 2010,
            'zillow_id': None,
            'zestimate_amount': Decimal('250000'),
            'zestimate_last_updated': date(day=25, month=3, year=2020),
            'address': '55 Evergreen',
            'city': 'Springfield',
            'state': 'CA',
            'zipcode': 91307
        }
        first_prop = Property.objects.create(**prop_data)

        request = self.get(first_prop.id)
        self.assertEqual(request.data['id'], 1)
        self.assertEqual(request.data['price'], '$250K')
        self.assertEqual(request.data['last_sold_date'], '03/25/2017')
        self.assertEqual(request.data['rentzestimate_last_updated'], '03/25/2020')
        self.assertEqual(request.data['zestimate_last_updated'], '03/25/2020')
        self.assertEqual(request.data['area_unit'], 'SqFt')
        self.assertEqual(request.data['home_type'], 'SingleFamily')
        self.assertEqual(request.data['bathrooms'], 2.50)
        self.assertEqual(request.data['bedrooms'], 4)
        self.assertEqual(request.data['home_size'], 4000)
        self.assertEqual(request.data['property_size'], 8000)
        self.assertEqual(request.data['link'], 'http://google.com')
        self.assertEqual(request.data['last_sold_price'], 250000.0000)
        self.assertEqual(request.data['rent_price'], None)
        self.assertEqual(request.data['rentzestimate_amount'], 1000.0000)
        self.assertEqual(request.data['tax_value'], 250000.0000)
        self.assertEqual(request.data['tax_year'], 2019)
        self.assertEqual(request.data['year_built'], 2010)
        self.assertEqual(request.data['zillow_id'], None)
        self.assertEqual(request.data['zestimate_amount'], 250000.0000)
        self.assertEqual(request.data['address'], '55 Evergreen')
        self.assertEqual(request.data['city'], 'Springfield')
        self.assertEqual(request.data['state'], 'CA')
        self.assertEqual(request.data['zipcode'], 91307)

    def test_list(self):
        for _ in range(5):
            prop_data = {
                'area_unit': AreaUnit.AREA_UNIT_SQFT,
                'home_type': HomeType.HOME_TYPE_SINGLE_FAMILY,
                'bathrooms': Decimal('2.5'),
                'bedrooms': 4,
                'home_size': 4000,
                'property_size': 8000,
                'link': 'http://google.com',
                'last_sold_date': date(day=25, month=3, year=2017),
                'last_sold_price': Decimal('250000'),
                'price': Decimal('250000'),
                'rent_price': None,
                'rentzestimate_amount': Decimal('1000'),
                'rentzestimate_last_updated': date(day=25, month=3, year=2020),
                'tax_value': Decimal('250000'),
                'tax_year': 2019,
                'year_built': 2010,
                'zillow_id': None,
                'zestimate_amount': Decimal('250000'),
                'zestimate_last_updated': date(day=25, month=3, year=2020),
                'address': '55 Evergreen',
                'city': 'Springfield',
                'state': 'CA',
                'zipcode': 91307
            }
            Property.objects.create(**prop_data)

        count = Property.objects.count()

        request = self.get_all()
        self.assertEqual(request.data['count'], count)

    def test_post(self):
        prop_data = {
            'area_unit': AreaUnit.AREA_UNIT_SQFT,
            'home_type': HomeType.HOME_TYPE_APARTMENT,
            'bathrooms': Decimal('1.5'),
            'bedrooms': 2,
            'home_size': 3000,
            'property_size': 3000,
            'link': 'http://google.com',
            'last_sold_date': date(day=25, month=3, year=2017),
            'last_sold_price': Decimal('250000'),
            'price': '$530K',
            'rentzestimate_amount': Decimal('1000'),
            'rentzestimate_last_updated': date(day=25, month=3, year=2020),
            'tax_value': Decimal('250000'),
            'tax_year': 2019,
            'year_built': 2010,
            'zestimate_amount': Decimal('250000'),
            'zestimate_last_updated': date(day=25, month=3, year=2020),
            'address': '55 Evergreen',
            'city': 'Springfield',
            'state': 'CA',
            'zipcode': 91307
        }

        request = self.post(data=prop_data)
        property_obj = Property.objects.order_by('-id').first()
        self.assertEqual(request.data['id'], property_obj.id)
        self.assertEqual(request.data['price'], '$530K')
        self.assertEqual(request.data['last_sold_date'], property_obj.last_sold_date.strftime('%m/%d/%Y'))
        self.assertEqual(request.data['rentzestimate_last_updated'],
                         property_obj.rentzestimate_last_updated.strftime('%m/%d/%Y'))
        self.assertEqual(request.data['zestimate_last_updated'],
                         property_obj.zestimate_last_updated.strftime('%m/%d/%Y'))
        self.assertEqual(request.data['area_unit'], property_obj.area_unit)
        self.assertEqual(request.data['home_type'], property_obj.home_type)
        self.assertEqual(request.data['bathrooms'], property_obj.bathrooms)
        self.assertEqual(request.data['bedrooms'], property_obj.bedrooms)
        self.assertEqual(request.data['home_size'], property_obj.home_size)
        self.assertEqual(request.data['property_size'], property_obj.property_size)
        self.assertEqual(request.data['link'], property_obj.link)
        self.assertEqual(request.data['last_sold_price'], property_obj.last_sold_price)
        self.assertEqual(request.data['rent_price'], property_obj.rent_price)
        self.assertEqual(request.data['rentzestimate_amount'], property_obj.rentzestimate_amount)
        self.assertEqual(request.data['tax_value'], property_obj.tax_value)
        self.assertEqual(request.data['tax_year'], property_obj.tax_year)
        self.assertEqual(request.data['year_built'], property_obj.year_built)
        self.assertEqual(request.data['zillow_id'], property_obj.zillow_id)
        self.assertEqual(request.data['zestimate_amount'], property_obj.zestimate_amount)
        self.assertEqual(request.data['address'], property_obj.address)
        self.assertEqual(request.data['city'], property_obj.city)
        self.assertEqual(request.data['state'], property_obj.state)
        self.assertEqual(request.data['zipcode'], 91307)

    def test_update(self):
        prop_data = {
            'area_unit': AreaUnit.AREA_UNIT_SQFT,
            'home_type': HomeType.HOME_TYPE_SINGLE_FAMILY,
            'bathrooms': Decimal('2.5'),
            'bedrooms': 4,
            'home_size': 4000,
            'property_size': 8000,
            'link': 'http://google.com',
            'last_sold_date': date(day=25, month=3, year=2017),
            'last_sold_price': Decimal('250000'),
            'price': Decimal('250000'),
            'rent_price': None,
            'rentzestimate_amount': Decimal('1000'),
            'rentzestimate_last_updated': date(day=25, month=3, year=2020),
            'tax_value': Decimal('250000'),
            'tax_year': 2019,
            'year_built': 2010,
            'zillow_id': None,
            'zestimate_amount': Decimal('250000'),
            'zestimate_last_updated': date(day=25, month=3, year=2020),
            'address': '55 Evergreen',
            'city': 'Springfield',
            'state': 'CA',
            'zipcode': 91307
        }
        property_obj = Property.objects.create(**prop_data)
        prop_data['zipcode'] = 91306
        prop_data['price'] = '$1.9M'
        self.put(property_obj.id, data=prop_data)
        property_obj.refresh_from_db()
        self.assertEqual(prop_data['price'], '$1.9M')
        self.assertEqual(prop_data['last_sold_date'], property_obj.last_sold_date)
        self.assertEqual(prop_data['rentzestimate_last_updated'], property_obj.rentzestimate_last_updated)
        self.assertEqual(prop_data['zestimate_last_updated'], property_obj.zestimate_last_updated)
        self.assertEqual(prop_data['area_unit'], property_obj.area_unit)
        self.assertEqual(prop_data['home_type'], property_obj.home_type)
        self.assertEqual(prop_data['bathrooms'], property_obj.bathrooms)
        self.assertEqual(prop_data['bedrooms'], property_obj.bedrooms)
        self.assertEqual(prop_data['home_size'], property_obj.home_size)
        self.assertEqual(prop_data['property_size'], property_obj.property_size)
        self.assertEqual(prop_data['link'], property_obj.link)
        self.assertEqual(prop_data['last_sold_price'], property_obj.last_sold_price)
        self.assertEqual(prop_data['rent_price'], property_obj.rent_price)
        self.assertEqual(prop_data['rentzestimate_amount'], property_obj.rentzestimate_amount)
        self.assertEqual(prop_data['tax_value'], property_obj.tax_value)
        self.assertEqual(prop_data['tax_year'], property_obj.tax_year)
        self.assertEqual(prop_data['year_built'], property_obj.year_built)
        self.assertEqual(prop_data['zillow_id'], property_obj.zillow_id)
        self.assertEqual(prop_data['zestimate_amount'], property_obj.zestimate_amount)
        self.assertEqual(prop_data['address'], property_obj.address)
        self.assertEqual(prop_data['city'], property_obj.city)
        self.assertEqual(prop_data['state'], property_obj.state)
        self.assertEqual(prop_data['zipcode'], 91306)

    def test_delete(self):
        prop_data = {
            'area_unit': AreaUnit.AREA_UNIT_SQFT,
            'home_type': HomeType.HOME_TYPE_SINGLE_FAMILY,
            'bathrooms': Decimal('2.5'),
            'bedrooms': 4,
            'home_size': 4000,
            'property_size': 8000,
            'link': 'http://google.com',
            'last_sold_date': date(day=25, month=3, year=2017),
            'last_sold_price': Decimal('250000'),
            'price': Decimal('250000'),
            'rent_price': None,
            'rentzestimate_amount': Decimal('1000'),
            'rentzestimate_last_updated': date(day=25, month=3, year=2020),
            'tax_value': Decimal('250000'),
            'tax_year': 2019,
            'year_built': 2010,
            'zillow_id': None,
            'zestimate_amount': Decimal('250000'),
            'zestimate_last_updated': date(day=25, month=3, year=2020),
            'address': '55 Evergreen',
            'city': 'Springfield',
            'state': 'CA',
            'zipcode': 91307
        }
        property_obj = Property.objects.create(**prop_data)
        self.delete(property_obj.id)
        self.assertEqual(Property.objects.filter(id=property_obj.id).first(), None)