from django.db.models import Model, CharField, DecimalField, DateField, IntegerField, URLField, TextChoices


class AreaUnit(TextChoices):
    AREA_UNIT_SQFT = 'SqFt', 'Square Feet'


class HomeType(TextChoices):
    HOME_TYPE_SINGLE_FAMILY = 'SingleFamily', 'Single Family'
    HOME_TYPE_VACANT_LAND = 'VacantResidentialLand', 'Vacant Residential Land'
    HOME_TYPE_MISC = 'Miscellaneous', 'Miscellaneous'
    HOME_TYPE_APARTMENT = 'Apartment', 'Condominium'
    HOME_TYPE_CONDO = 'Condominium', 'Condominium'
    HOME_TYPE_DUPLEX = 'Duplex', 'Duplex'
    HOME_TYPE_MULTI_FAMILY = 'MultiFamily2To4', 'Multi-Family 2 to 4'


class Property(Model):
    area_unit = CharField(max_length=32, choices=AreaUnit.choices, default=AreaUnit.AREA_UNIT_SQFT,
                          help_text='unit used to define measurements.')
    home_type = CharField(max_length=32, choices=HomeType.choices, default=HomeType.HOME_TYPE_SINGLE_FAMILY,
                          help_text='Home Type')
    bathrooms = DecimalField(decimal_places=2, max_digits=6, null=True, blank=True, help_text='Number of bathrooms')
    bedrooms = IntegerField(null=True, blank=True, help_text='Number of bedrooms')
    home_size = IntegerField(null=True, blank=True, help_text='Home Size')
    property_size = IntegerField(null=True, blank=True, help_text='Property Size')
    link = URLField(null=True, blank=True, help_text='URL for listing')

    last_sold_date = DateField(null=True, blank=True, help_text='Last Sold Date', )
    last_sold_price = DecimalField(decimal_places=4, max_digits=13, null=True, blank=True, help_text='Last Sold Price')
    price = DecimalField(decimal_places=4, max_digits=13, null=True, blank=True, help_text='Current Property Price')
    rent_price = DecimalField(decimal_places=4, max_digits=10, null=True, blank=True, help_text='Rent Price')
    rentzestimate_amount = DecimalField(decimal_places=4, max_digits=13, null=True, blank=True,
                                        help_text='Estimated Rent Price')
    rentzestimate_last_updated = DateField(null=True, blank=True, help_text='Estimated Rent Price Last Update')
    tax_value = DecimalField(decimal_places=4, max_digits=13, null=True, blank=True, help_text='Tax Value')
    tax_year = IntegerField(null=True, blank=True, help_text='Tax Year')
    year_built = IntegerField(null=True, blank=True, help_text='Year Built')
    zillow_id = IntegerField(null=True, blank=True, help_text='Zillow ID')
    zestimate_amount = DecimalField(decimal_places=4, max_digits=13, null=True, blank=True, help_text='Zillow Estimate')
    zestimate_last_updated = DateField(null=True, blank=True, help_text='Zillow Estimate')

    address = CharField(max_length=255, help_text='Street Address')
    city = CharField(max_length=128, help_text='City')
    state = CharField(max_length=8, help_text='State')
    zipcode = IntegerField(help_text='Zip Code')
