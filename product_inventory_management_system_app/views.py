from django.shortcuts import render
from .models import Brand , Color , Product , Store , Inventory
from django.contrib.auth.models import User
from django.http import HttpResponse
from .serializers import BrandSerializer , ColorSerializer , ProductSerializer , StoreSerializer , InventorySerializer , UserSerializer , CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics , status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from django.shortcuts import get_object_or_404
from django.core.exceptions import MultipleObjectsReturned
from .resources import ProductResource
from drf_yasg.utils import swagger_auto_schema


class BrandCreateAPIView(generics.GenericAPIView):
    brand_serializer_class = BrandSerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        responses={201: 'Created', 400: 'Bad Request'},
        operation_summary='Create a brand',
        operation_description='Create a new brand'
    )

    def post(self , request , *args , **kwargs):
        brand_serializer = self.brand_serializer_class(data=request.data)
        if brand_serializer.is_valid():
            brand_serializer.save()
            return Response({'message' : 'Brand has been created successfully'} , status=status.HTTP_201_CREATED)
        return Response(brand_serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class BrandListAPIView(generics.GenericAPIView):
    brand_serializer_class = BrandSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={200: 'OK', 400: 'Bad Request'},
        operation_summary='Get all brands',
        operation_description='Retrieve a list of all brands'
    )

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
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        responses={200: 'OK', 400: 'Bad Request'},
        operation_summary='Update a brand',
        operation_description='Update an existing brand by providing its ID and new data'
    )

    def put(self , request , *args , **kwargs):
        brand = self.get_object()
        brand_serializer = self.brand_serializer_class(brand , data=request.data , partial=True)
        if brand_serializer.is_valid():
            brand_serializer.save()
            return Response({'message' : 'Brand has been updated successfully'} , status=status.HTTP_200_OK)
        return Response(brand_serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class BrandDeleteAPIView(generics.GenericAPIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        responses={200: 'OK', 400: 'Bad Request'},
        operation_summary='Delete a brand',
        operation_description='Delete an existing brand by providing its ID'
    )

    def delete(self , request , pk ,*args , **kwargs):
        brand = Brand.objects.filter(pk=pk)
        brand.delete()
        return Response({'message' : 'Brand has been deleted successfully'} , status=status.HTTP_200_OK)


class ColorCreateAPIView(generics.GenericAPIView):
    color_serializer_class = ColorSerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        responses={201: 'Created', 400: 'Bad Request'},
        operation_summary='Create a color',
        operation_description='Create a new color'
    )

    def post(self , request , *args , **kwargs):
        color_serializer = self.color_serializer_class(data=request.data)
        if color_serializer.is_valid():
            color_serializer.save()
            return Response({'message' : 'Color has been created successfully'} , status=status.HTTP_201_CREATED)
        return Response(color_serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class ColorListAPIView(generics.GenericAPIView):
    color_serializer_class = ColorSerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        responses={200: 'OK', 400: 'Bad Request'},
        operation_summary='Get all colors',
        operation_description='Retrieve a list of all colors'
    )

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
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        responses={200: 'OK', 400: 'Bad Request'},
        operation_summary='Update a color',
        operation_description='Update an existing color by providing its ID and new data'
    )

    def put(self , request , *args , **kwargs):
        color = self.get_object()
        color_serializer = self.color_serializer_class(color , data=request.data , partial=True)
        if color_serializer.is_valid():
            color_serializer.save()
            return Response({'message' : 'Color has been updated successfully'} , status=status.HTTP_200_OK)
        return Response(color_serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class ColorDeleteAPIView(generics.GenericAPIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        responses={200: 'OK', 400: 'Bad Request'},
        operation_summary='Delete a color',
        operation_description='Delete an existing color by providing its ID'
    )

    def delete(self , request , pk ,*args , **kwargs):
        color = Color.objects.filter(pk=pk)
        color.delete()
        return Response({'message' : 'Color has been deleted successfully'} , status=status.HTTP_200_OK)

class ProductCreateAPIView(generics.GenericAPIView):
    product_serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        responses={201: 'Created', 400: 'Bad Request'},
        operation_summary='Create a product',
        operation_description='Create a new product'
    )

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
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={200: 'OK', 400: 'Bad Request'},
        operation_summary='Get all products',
        operation_description='Retrieve a list of all products'
    )
    
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

class ProductUpdateAPIView(generics.GenericAPIView):
    queryset = Product.objects.all()
    product_serializer_class  = ProductSerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        responses={200: 'OK', 400: 'Bad Request'},
        operation_summary='Update a product',
        operation_description='Update an existing product by providing its ID and new data'
    )

    def put(self , request , *args , **kwargs):
        product = self.get_object()
        product_serializer = self.product_serializer_class(product , data=request.data , partial=True)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response({'message' : 'Product has been updated successfully'} , status=status.HTTP_200_OK)
        return Response(product_serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class ProductDeleteAPIView(generics.GenericAPIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        responses={200: 'OK', 400: 'Bad Request'},
        operation_summary='Delete a product',
        operation_description='Delete an existing product by providing its ID'
    )

    def delete(self , request , pk , *args , **kwargs):
        product = Product.objects.filter(pk = pk)
        product.delete()
        return Response({'message' : 'Product has been deleted successfully'} , status=status.HTTP_200_OK)

class StoreCreateAPIView(generics.GenericAPIView):
    store_serializer_class = StoreSerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        responses={201: 'Created', 400: 'Bad Request'},
        operation_summary='Create a store',
        operation_description='Create a new store'
    )

    def post(self , request , *args , **kwargs):
        store_serializer = self.store_serializer_class(data=request.data)
        if store_serializer.is_valid():
            store_serializer.save()
            return Response({'message' : 'Store has been created successfully'} , status=status.HTTP_201_CREATED)
        return Response(store_serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class StoreListAPIView(generics.GenericAPIView):
    store_serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={200: 'OK', 400: 'Bad Request'},
        operation_summary='Get all stores',
        operation_description='Retrieve a list of all stores'
    )

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
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        responses={200: 'OK', 400: 'Bad Request'},
        operation_summary='Update a store',
        operation_description='Update an existing store by providing its ID and new data'
    )

    def put(self , request , *args , **kwargs):
        store = self.get_object()
        store_serializer = self.store_serializer_class(store , data=request.data , partial=True)
        if store_serializer.is_valid():
            store_serializer.save()
            return Response({'message' : 'Store has been updated successfully'} , status=status.HTTP_200_OK)
        return Response(store_serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class StoreDeleteAPIView(generics.GenericAPIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        responses={200: 'OK', 400: 'Bad Request'},
        operation_summary='Delete a store',
        operation_description='Delete an existing store by providing its ID'
    )
    

    def delete(self , request , pk , *args , **kwargs):
        store = Store.objects.filter(pk=pk)
        store.delete()
        return Response({'message' : 'Store has been deleted successfully'} , status=status.HTTP_200_OK)

class InventoryCreateAPIView(generics.GenericAPIView):
    inventory_serializer_class = InventorySerializer  
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        responses={201: 'Created', 400: 'Bad Request'},
        operation_summary='Create a inventory',
        operation_description='Create a new inventory'
    )

    def post(self, request, *args, **kwargs):
        inventory_serializer = self.inventory_serializer_class(data=request.data)
        if inventory_serializer.is_valid():           
            product_name = request.data.get('product_name')
            store_name = request.data.get('store_name')       
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

            return Response({'message': 'Inventory has been created successfully'} , status=status.HTTP_201_CREATED)
        return Response(inventory_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class InventoryListAPIView(generics.GenericAPIView):
    inventory_serializer_class = InventorySerializer
    product_serializer_class = ProductSerializer
    store_serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={200: 'OK', 400: 'Bad Request'},
        operation_summary='Get all inventories',
        operation_description='Retrieve a list of all inventories'
    )
    
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
                'quantity': inventory_data['quantity'],
                'last_stocked_date': inventory_data['last_stocked_date'],
                'is_available': inventory_data['is_available'],
            })

        context = {
            'Total Inventories': inventory.count(),
            'Inventories': inventory_list
        }

        return Response(context, status=status.HTTP_200_OK)
    
class InventoryUpdateAPIView(generics.GenericAPIView):
    queryset = Inventory.objects.all()
    inventory_serializer_class = InventorySerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        responses={200: 'OK', 400: 'Bad Request'},
        operation_summary='Update an inventory',
        operation_description='Update an existing inventory by providing its ID and new data'
    )

    def put(self , request , *args , **kwargs):
        inventory = self.get_object()
        inventory_serializer = self.inventory_serializer_class(inventory , data=request.data , partial=True)
        if inventory_serializer.is_valid():
            inventory_serializer.save()
            return Response({'message' : 'Inventory has been updated successfully'} , status=status.HTTP_200_OK)
        return Response(inventory_serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class InventoryDeleteAPIView(generics.GenericAPIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        responses={200: 'OK', 400: 'Bad Request'},
        operation_summary='Delete an inventory',
        operation_description='Delete an existing inventory by providing its ID'
    )

    def delete(self , request , pk , *args , **kwargs):
        inventory = Inventory.objects.filter(pk = pk)
        inventory.delete()
        return Response({"message" : "Inventory has been deleted successfully"} , status=status.HTTP_200_OK)


class UserCreateAPIView(generics.GenericAPIView):
     user_serializer_class = UserSerializer
     permission_classes = [IsAuthenticated]

     @swagger_auto_schema(
        responses={201: 'Created', 400: 'Bad Request'},
        operation_summary='Create a user',
        operation_description='Create a new user'
    )

     def post(self , request , *args , **kwargs):
        user_serializer = self.user_serializer_class(data=request.data)
        if user_serializer.is_valid():
            email = user_serializer.validated_data['email']
            if User.objects.filter(email=email).exists():
                return Response({'message': 'Email already exists'})
            password = user_serializer.validated_data['password']
            user = user_serializer.save()
            user.set_password(password)
            user.save()
            return Response({'message' : 'User has been created successfully'} , status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors , status=status.HTTP_400_BAD_REQUEST)
     
class UserListAPIView(generics.GenericAPIView):
    user_serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        responses={200: 'OK', 400: 'Bad Request'},
        operation_summary='Get all users',
        operation_description='Retrieve a list of all users'
    )

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
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={200: 'OK', 400: 'Bad Request'},
        operation_summary='Update a user',
        operation_description='Update an existing user by providing its ID and new data'
    )

    def put(self , request , *args , **kwargs):
        user = self.get_object()
        user_serializer = self.user_serializer_class(user , data=request.data , partial=True)
        if user_serializer.is_valid():
            password = user_serializer.validated_data.get('password')
            if password:
                user.set_password(password)
            user = user_serializer.save()
            return Response({'message' : 'User has been updated successfully'} , status=status.HTTP_200_OK)
        return Response(user.errors , status=status.HTTP_400_BAD_REQUEST)
    
class UserDeleteAPIView(generics.GenericAPIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        responses={200: 'OK', 400: 'Bad Request'},
        operation_summary='Delete a user',
        operation_description='Delete an existing user by providing its ID'
    )

    def delete(self , request , pk , *args , **kwargs):
        user = User.objects.filter(pk = pk)
        user.delete()
        return Response({"message" : "User has been deleted successfully"} , status=status.HTTP_200_OK)
    
class CustomTokenObtainPairView(TokenObtainPairView):
    token_serializer_class = CustomTokenObtainPairSerializer

    swagger_auto_schema(
        operation_summary='JWT Authentication',
        operation_description='Generate refresh and access token'
    ) 


class ExportProductToXLSXAPIView(generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = None
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        responses={200: 'OK', 400: 'Bad Request'},
        operation_summary='Retrieve a list of all products',
        operation_description='Export products to XLSX file'
    )

    def get(self, request, *args, **kwargs):
        dataset = ProductResource().export(self.get_queryset())
        response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="products.xlsx"'
        return response

class ExportProductToCSVAPIView(generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = None
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        responses={200: 'OK', 400: 'Bad Request'},
        operation_summary='Retrieve a list of all products',
        operation_description='Export products to CSV file'
    )

    def get(self, request, *args, **kwargs):
        dataset = ProductResource().export(self.get_queryset())
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="products.csv"'
        return response