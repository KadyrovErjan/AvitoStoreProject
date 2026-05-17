from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size = 5

class SubCategoryPagination(PageNumberPagination):
    page_size = 3