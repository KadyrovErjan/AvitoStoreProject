from .views import (UserProfileViewSet, CategoryListAPIView, SubCategoryListAPIView,
                    ProductListAPIView, ProductDetailAPIView, ReviewViewSet,
                    CategoryDetailAPIView, SubCategoryDetailAPIView, RegisterView, CustomLoginView, LogoutView,
                    CartAPIView, CartItemViewSet, FavoriteItemViewSet, FavoriteAPIView)
from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users')
router.register(r'review', ReviewViewSet, basename='review')


urlpatterns = [
    path('', include(router.urls)),
    path('product/', ProductListAPIView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('sub_category/', SubCategoryListAPIView.as_view(), name='subcategory_list'),
    path('sub_category/<int:pk>/', SubCategoryDetailAPIView.as_view(), name='subcategory_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cart/', CartAPIView.as_view(), name='cart_detail'),
    path('cart_item/', CartItemViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('cart_item/<int:pk>/', CartItemViewSet.as_view({'put': 'update', 'delete': 'destroy'})),
    path('favorite/', FavoriteAPIView.as_view(), name='favorite_detail'),
    path('favorite_item/', FavoriteItemViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('favorite_item/<int:pk>', FavoriteItemViewSet.as_view({'delete': 'destroy'}))



]