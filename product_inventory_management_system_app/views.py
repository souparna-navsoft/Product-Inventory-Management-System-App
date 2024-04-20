from django.shortcuts import render
from .models import Brand , Color , Product , Store , Inventory
from django.contrib.auth.models import User
from .serializers import BrandSerializer , ColorSerializer , ProductSerializer , StoreSerializer , InventorySerializer , UserSerializer , CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics , status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.exceptions import MultipleObjectsReturned


class BrandCreateAPIView(generics.GenericAPIView):
    brand_serializer_class = BrandSerializer

    def post(self , request , *args , **kwargs):
        brand_serializer = self.brand_serializer_class(data=request.data)
        if brand_serializer.is_valid():
            brand_serializer.save()
            return Response({'message' : 'Brand has been created successfully'} , status=status.HTTP_201_CREATED)
        return Response(brand_serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class BrandListAPIView(generics.GenericAPIView):
    brand_serializer_class = BrandSerializer

    def get(self , request , *args , **kwargs):
        brand = Brand.objects.all()
        brand_serializer = self.brand_serializer_class(brand , many=True)
        context = {
            'Total Brands' : brand.count(),
            'Brands' : brand_serializer.data
        }
        return Response(context , status=status.HTTP_200_OK)

class BrandUpdateAPIView(generics.GenericAPIView):
    queryset = Brand.objects.all()
    brand_serializer_class  = BrandSerializer

    def put(self , request , *args , **kwargs):
        brand = self.get_object()
        brand_serializer = self.brand_serializer_class(brand , data=request.data , partial=True)
        if brand_serializer.is_valid():
            brand_serializer.save()
            return Response({'message' : 'Brand has been updated successfully'} , status=status.HTTP_200_OK)
        return Response(brand_serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class BrandDeleteAPIView(generics.GenericAPIView):

    def delete(self , request , pk ,*args , **kwargs):
        brand = Brand.objects.filter(pk=pk)
        brand.delete()
        return Response({'message' : 'Brand has been deleted successfully'} , status=status.HTTP_200_OK)


class ColorCreateAPIView(generics.GenericAPIView):
    color_serializer_class = ColorSerializer

    def post(self , request , *args , **kwargs):
        color_serializer = self.color_serializer_class(data=request.data)
        if color_serializer.is_valid():
            color_serializer.save()
            return Response({'message' : 'Color has been created successfully'} , status=status.HTTP_201_CREATED)
        return Response(color_serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class ColorListAPIView(generics.GenericAPIView):
    color_serializer_class = ColorSerializer

    def get(self , request , *args , **kwargs):
        color = Color.objects.all()
        color_serializer = self.color_serializer_class(color , many=True)
        context = {
            'Total Colors' : color.count(),
            'Colors' : color_serializer.data
        }
        return Response(context , status=status.HTTP_200_OK)
    
class ColorUpdateAPIView(generics.GenericAPIView):
    queryset = Color.objects.all()
    color_serializer_class  = ColorSerializer

    def put(self , request , *args , **kwargs):
        color = self.get_object()
        color_serializer = self.color_serializer_class(color , data=request.data , partial=True)
        if color_serializer.is_valid():
            color_serializer.save()
            return Response({'message' : 'Color has been updated successfully'} , status=status.HTTP_200_OK)
        return Response(color_serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class ColorDeleteAPIView(generics.GenericAPIView):

    def delete(self , request , pk ,*args , **kwargs):
        color = Color.objects.filter(pk=pk)
        color.delete()
        return Response({'message' : 'Color has been deleted successfully'} , status=status.HTTP_200_OK)

class ProductCreateAPIView(generics.GenericAPIView):
    product_serializer_class = ProductSerializer  

    def post(self, request, *args, **kwargs):
        product_serializer = self.product_serializer_class(data=request.data)
        if product_serializer.is_valid():           
            brand_name = request.data.get('brand')
            color_name = request.data.get('color')           
            brand, _ = Brand.objects.get_or_create(name=brand_name)
            color, _ = Color.objects.get_or_create(name=color_name)
            product_serializer.save(brand=brand, color=color)
            print(product_serializer)
            return Response({'message' : 'Product has been created successfully'} , status=status.HTTP_201_CREATED)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductListAPIView(generics.GenericAPIView):
    product_serializer_class = ProductSerializer
    brand_serializer_class = BrandSerializer
    color_serializer_class = ColorSerializer
    
    def get(self, request, *args, **kwargs):
        product = Product.objects.all()
        product_serializer = self.product_serializer_class(product, many=True)
        serialized_product = product_serializer.data
        print(serialized_product)
        product_list = []

        for product_data in serialized_product:
            brand_name = product_data['brand_name']
            color_name = product_data['color_name']
            product_list.append({
                'id': product_data['id'],
                'sku': product_data['sku'],
                'name': product_data['name'],
                'brand_name': brand_name,
                'color_name': color_name,
                'price': product_data['price'],
                'description': product_data['description'],
                'reviews': product_data['reviews']
            })

        context = {
            'Total Products': product.count(),
            'Products': product_list
        }

        return Response(context, status=status.HTTP_200_OK)
    

class StoreCreateAPIView(generics.GenericAPIView):
    store_serializer_class = StoreSerializer

    def post(self , request , *args , **kwargs):
        store_serializer = self.store_serializer_class(data=request.data)
        if store_serializer.is_valid():
            store_serializer.save()
            return Response({'message' : 'Store has been created successfully'} , status=status.HTTP_201_CREATED)
        return Response(store_serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class StoreListAPIView(generics.GenericAPIView):
    store_serializer_class = StoreSerializer

    def get(self , request , *args , **kwargs):
        store = Store.objects.all()
        store_serializer = self.store_serializer_class(store , many=True)
        context = {
            'Total Stores' : store.count(),
            'Stores' : store_serializer.data
        }
        return Response(context , status=status.HTTP_200_OK)
    
class StoreUpdateAPIView(generics.GenericAPIView):
    queryset = Store.objects.all()
    store_serializer_class = StoreSerializer

    def put(self , request , *args , **kwargs):
        store = self.get_object()
        store_serializer = self.store_serializer_class(store , data=request.data , partial=True)
        if store_serializer.is_valid():
            store_serializer.save()
            return Response({'message' : 'Store has been updated successfully'} , status=status.HTTP_200_OK)
        return Response(store_serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class StoreDeleteAPIView(generics.GenericAPIView):
    def delete(self , request , pk , *args , **kwargs):
        store = Store.objects.filter(pk=pk)
        store.delete()
        return Response({'message' : 'Store has been deleted successfully'} , status=status.HTTP_200_OK)

class InventoryCreateAPIView(generics.GenericAPIView):
    inventory_serializer_class = InventorySerializer  

    def post(self, request, *args, **kwargs):
        inventory_serializer = self.inventory_serializer_class(data=request.data)
        if inventory_serializer.is_valid():           
            product_name = request.data.get('product_name')
            store_name = request.data.get('store_name')       
            print('-----------------------', product_name)   
            print('-----------------------', store_name) 

            try:
                product = Product.objects.get(name=product_name)
            except Product.DoesNotExist:
                product = Product.objects.create(name=product_name)
            except Product.MultipleObjectsReturned:
                product = Product.objects.filter(name=product_name).first()

            try:
                store = Store.objects.get(name=store_name)
            except Store.DoesNotExist:
                store = Store.objects.create(name=store_name)
            except Store.MultipleObjectsReturned:
                store = Store.objects.filter(name=store_name).first()

            inventory_instance = inventory_serializer.create({
                'product': product,
                'store': store,
                'quantity': request.data.get('quantity'), 
                'last_stocked_date': request.data.get('last_stocked_date'), 
                'is_available': request.data.get('is_available'),  
            })

            print(inventory_serializer)
            return Response({'message': 'Inventory has been created successfully'}, status=status.HTTP_201_CREATED)
        return Response(inventory_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class InventoryListAPIView(generics.GenericAPIView):
    inventory_serializer_class = InventorySerializer
    product_serializer_class = ProductSerializer
    store_serializer_class = StoreSerializer
    
    def get(self, request, *args, **kwargs):
        inventory = Inventory.objects.all()
        inventory_serializer = self.inventory_serializer_class(inventory, many=True)
        serialized_inventory = inventory_serializer.data

        inventory_list = []

        for inventory_data in serialized_inventory:
            product_name = inventory_data['product_name']
            store_name = inventory_data['store_name']
            inventory_list.append({
                'id': inventory_data['id'],
                'product_name': product_name,
                'store_name': store_name,
                'last_stocked_date': inventory_data['last_stocked_date'],
                'is_available': inventory_data['is_available'],
            })

        context = {
            'Total Inventories': inventory.count(),
            'Inventories': inventory_list
        }

        return Response(context, status=status.HTTP_200_OK)
    
class UserCreateAPIView(generics.GenericAPIView):
     user_serializer_class = UserSerializer

     def post(self , request , *args , **kwargs):
        user_serializer = self.user_serializer_class(data=request.data)
        if user_serializer.is_valid():
            password = user_serializer.validated_data['password']
            user = user_serializer.save()
            user.set_password(password)
            user.save()
            context = {
                'id' : user.id,
                'username' : user.username,
                'first_name' : user.first_name,
                'last_name' : user.last_name,
                'email' : user.email,
                'password' : user.password
            }
            return Response({'message' : 'User has been created successfully'} , status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors , status=status.HTTP_400_BAD_REQUEST)
     
class UserListAPIView(generics.GenericAPIView):
    user_serializer_class = UserSerializer

    def get(self , request , *args , **kwargs):
        user = User.objects.all()
        user_serializer = self.user_serializer_class(user , many=True)
        context = {
            'Total Users' : user.count(),
            'Users' : user_serializer.data
        }
        return Response(context , status=status.HTTP_200_OK)

class UserUpdateAPIView(generics.GenericAPIView):
    queryset = User.objects.all()
    user_serializer_class = UserSerializer

    def put(self , request , *args , **kwargs):
        user = self.get_object()
        user_serializer = self.user_serializer_class(user , data=request.data , partial=True)
        if user_serializer.is_valid():
            password = user_serializer.validated_data['password']
            user = user_serializer.save()
            user.set_password(password)
            user.save()
            context = {
                'id' : user.id,
                'username' : user.username,
                'first_name' : user.first_name,
                'last_name' : user.last_name,
                'email' : user.email,
                'password' : user.password
            }
            return Response({'message' : 'User has been updated successfully'} , status=status.HTTP_200_OK)
        return Response(user.errors , status=status.HTTP_400_BAD_REQUEST)
    
class UserDeleteAPIView(generics.GenericAPIView):
    def delete(self , request , pk , *args , **kwargs):
        user = User.objects.filter(pk = pk)
        user.delete()
        return Response({"message" : "User has been deleted successfully"} , status=status.HTTP_200_OK)
    
class CustomTokenObtainPairView(TokenObtainPairView):
    token_serializer_class = CustomTokenObtainPairSerializer