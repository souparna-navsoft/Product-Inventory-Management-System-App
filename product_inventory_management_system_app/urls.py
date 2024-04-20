from django.urls import path
from .views import BrandCreateAPIView , BrandListAPIView , BrandUpdateAPIView , BrandDeleteAPIView , ColorCreateAPIView , ColorListAPIView , ColorUpdateAPIView , ColorDeleteAPIView , ProductCreateAPIView , ProductListAPIView , StoreCreateAPIView , StoreListAPIView , StoreUpdateAPIView , InventoryCreateAPIView , InventoryListAPIView , UserCreateAPIView , UserListAPIView , UserUpdateAPIView , UserDeleteAPIView , CustomTokenObtainPairView

urlpatterns = [
    path('createbrand/' , BrandCreateAPIView.as_view() , name='create-brand'),
    path('listbrand/' , BrandListAPIView.as_view() , name='list-brand'),
    path('updatebrand/<int:pk>/' , BrandUpdateAPIView.as_view() , name='update-brand'),
    path('deletebrand/<int:pk>/' , BrandDeleteAPIView.as_view() , name='delete-brand'),
    path('createcolor/' , ColorCreateAPIView.as_view() , name='create-color'),
    path('listcolor/' , ColorListAPIView.as_view() , name='list-color'),
    path('updatecolor/<int:pk>/' , ColorUpdateAPIView.as_view() , name='update-color'),
    path('deletecolor/<int:pk>/' , ColorDeleteAPIView.as_view() , name='delete-color'),
    path('createproduct/' , ProductCreateAPIView.as_view() , name='create-product'),
    path('listproduct/' , ProductListAPIView.as_view() , name='list-product'),
    path('createstore/' , StoreCreateAPIView.as_view() , name='create-store'),
    path('liststore/' , StoreListAPIView.as_view() , name='list-store'),
    path('updatestore/<int:pk>/' , StoreUpdateAPIView.as_view() , name='update-store'),
    path('createinventory/' , InventoryCreateAPIView.as_view() , name='create-inventory'),
    path('listinventory/' , InventoryListAPIView.as_view() , name='list-inventory'),
    path('createuser/' , UserCreateAPIView.as_view() , name='create-user'),
    path('listuser/' , UserListAPIView.as_view() , name='list-user'),
    path('updateuser/<int:pk>/' , UserUpdateAPIView.as_view() , name='update-user'),
    path('deleteuser/<int:pk>/' , UserDeleteAPIView.as_view() , name='delete-user'),
    path('api/token/' , CustomTokenObtainPairView.as_view() , name='api-token')
]
