import re
from decimal import Decimal

from rest_framework.serializers import Field, DecimalField


class ShortenedPrice(Field):
    MULTIPLIER = {
        'M': {
            'multiplier': 1000000,
            'precision': 2
        },
        'K': {
            'multiplier': 1000,
            'precision': 0
        },
    }

    def to_representation(self, value):
        for suffix, mult_val in reversed(sorted([(suf, mult) for suf, mult in self.MULTIPLIER.items()],
                                                key=lambda x: x[1]['multiplier'])):
            multiplier = mult_val['multiplier']
            precision = mult_val['precision']
            if value // mult_val['multiplier']:
                return f'${value/multiplier:.{precision}f}{suffix}'

        return f'${value:.0f}'

    def to_internal_value(self, data):
        multiplier_regex = ''.join(self.MULTIPLIER.keys())
        regex = re.compile(fr'([$])([0-9.]+)([{multiplier_regex}])')

        re_matches = regex.findall(data)

        if re_matches:
            return Decimal(re_matches[0][1]) * self.MULTIPLIER[re_matches[0][2]]['multiplier']

        return None