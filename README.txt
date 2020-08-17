Property API
GET/POST/PUT/DELETE are all supported

To retrieve a group of properties:
GET /api/properties/?page=<PAGE_NUMBER>

To retrieve a specific property
GET /api/properties/<ID>/

To create a property
POST /api/properties/ with data as json and fields defined as

    "id": {
        "type": "integer",
        "required": false,
        "read_only": true,
        "label": "ID"
    },
    "price": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Price",
        "format": "$<VAL><K|M>"
    },
    "last_sold_date": {
        "type": "date",
        "required": false,
        "read_only": false,
        "label": "Last sold date",
        "format": "%m/%d/%Y"
    },
    "rentzestimate_last_updated": {
        "type": "date",
        "required": false,
        "read_only": false,
        "label": "Rentzestimate last updated",
        "format": "%m/%d/%Y"
    },
    "zestimate_last_updated": {
        "type": "date",
        "required": false,
        "read_only": false,
        "label": "Zestimate last updated",
        "format": "%m/%d/%Y"
    },
    "area_unit": {
        "type": "choice",
        "required": false,
        "read_only": false,
        "label": "Area unit",
        "help_text": "unit used to define measurements.",
        "choices": [
            {
                "value": "SqFt",
                "display_name": "Square Feet"
            }
        ]
    },
    "home_type": {
        "type": "choice",
        "required": false,
        "read_only": false,
        "label": "Home type",
        "help_text": "Home Type",
        "choices": [
            {
                "value": "SingleFamily",
                "display_name": "Single Family"
            },
            {
                "value": "VacantResidentialLand",
                "display_name": "Vacant Residential Land"
            },
            {
                "value": "Miscellaneous",
                "display_name": "Miscellaneous"
            },
            {
                "value": "Apartment",
                "display_name": "Condominium"
            },
            {
                "value": "Condominium",
                "display_name": "Condominium"
            },
            {
                "value": "Duplex",
                "display_name": "Duplex"
            },
            {
                "value": "MultiFamily2To4",
                "display_name": "Multi-Family 2 to 4"
            }
        ]
    },
    "bathrooms": {
        "type": "decimal",
        "required": false,
        "read_only": false,
        "label": "Bathrooms",
        "help_text": "Number of bathrooms"
    },
    "bedrooms": {
        "type": "integer",
        "required": false,
        "read_only": false,
        "label": "Bedrooms",
        "help_text": "Number of bedrooms"
    },
    "home_size": {
        "type": "integer",
        "required": false,
        "read_only": false,
        "label": "Home size",
        "help_text": "Home Size"
    },
    "property_size": {
        "type": "integer",
        "required": false,
        "read_only": false,
        "label": "Property size",
        "help_text": "Property Size"
    },
    "link": {
        "type": "url",
        "required": false,
        "read_only": false,
        "label": "Link",
        "help_text": "URL for listing",
        "max_length": 200
    },
    "last_sold_price": {
        "type": "decimal",
        "required": false,
        "read_only": false,
        "label": "Last sold price",
        "help_text": "Last Sold Price"
    },
    "rent_price": {
        "type": "decimal",
        "required": false,
        "read_only": false,
        "label": "Rent price",
        "help_text": "Rent Price"
    },
    "rentzestimate_amount": {
        "type": "decimal",
        "required": false,
        "read_only": false,
        "label": "Rentzestimate amount",
        "help_text": "Estimated Rent Price"
    },
    "tax_value": {
        "type": "decimal",
        "required": false,
        "read_only": false,
        "label": "Tax value",
        "help_text": "Tax Value"
    },
    "tax_year": {
        "type": "integer",
        "required": false,
        "read_only": false,
        "label": "Tax year",
        "help_text": "Tax Year"
    },
    "year_built": {
        "type": "integer",
        "required": false,
        "read_only": false,
        "label": "Year built",
        "help_text": "Year Built"
    },
    "zillow_id": {
        "type": "integer",
        "required": false,
        "read_only": false,
        "label": "Zillow id",
        "help_text": "Zillow ID"
    },
    "zestimate_amount": {
        "type": "decimal",
        "required": false,
        "read_only": false,
        "label": "Zestimate amount",
        "help_text": "Zillow Estimate"
    },
    "address": {
        "type": "string",
        "required": true,
        "read_only": false,
        "label": "Address",
        "help_text": "Street Address",
        "max_length": 255
    },
    "city": {
        "type": "string",
        "required": true,
        "read_only": false,
        "label": "City",
        "help_text": "City",
        "max_length": 128
    },
    "state": {
        "type": "string",
        "required": true,
        "read_only": false,
        "label": "State",
        "help_text": "State",
        "max_length": 8
    },
    "zipcode": {
        "type": "integer",
        "required": true,
        "read_only": false,
        "label": "Zipcode",
        "help_text": "Zip Code"
    }

To update:
PUT /api/properties/<ID>/ with date as defined similary to property creation

To import a csv use:
python manage.py insert_csv <CSV_FILE_PATH>