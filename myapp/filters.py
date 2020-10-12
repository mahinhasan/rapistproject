import django_filters
from .models import Rapiest

class SinppetFilter(django_filters.FilterSet):
    class Meta:
        model = Rapiest
        fields = ['name']