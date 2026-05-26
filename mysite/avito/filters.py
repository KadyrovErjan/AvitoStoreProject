from django_filters import FilterSet
from mysite.models import Product

class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'product_type': ['exact'],
            'subcategory': ['exact'],
            'price': ['gt', 'lt']
        }
