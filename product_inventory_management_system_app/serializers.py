from rest_framework import serializers
from .models import Brand , Color , Product , Store , Inventory
from django.contrib.auth.models import User


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id' , 'name' , 'country' , 'founded_year' , 'description']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id' , 'name' , 'description']

class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    color_name = serializers.CharField(source='color.name', read_only=True)
  

    class Meta:
        model = Product
        fields = ['id', 'sku', 'name', 'brand_name' , 'color_name' , 'price' , 'description', 'reviews']

    def create(self, validated_data):
        brand_name = validated_data.pop('brand_name', None)
        color_name = validated_data.pop('color_name', None)

        if brand_name:
            brand, _ = Brand.objects.get_or_create(name=brand_name)
            validated_data['brand'] = brand

        if color_name:
            color, _ = Color.objects.get_or_create(name=color_name)
            validated_data['color'] = color

        return super().create(validated_data)

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id' , 'name' , 'address' , 'phone_number' , 'email' , 'rating']

class InventorySerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    store_name = serializers.CharField(source='store.name', read_only=True)

    class Meta:
        model = Inventory
        fields = ['id','product_name' , 'store_name' , 'quantity' , 'last_stocked_date' , 'is_available']

        def create(self, validated_data):
            product_name = validated_data.pop('product_name', None)
            store_name = validated_data.pop('store_name', None)

            if product_name:
                product, _ = product.objects.get_or_create(name=product_name)
                validated_data['product'] = product

            if store_name:
                store, _ = store.objects.get_or_create(name=store_name)
                validated_data['store'] = store

            return super().create(validated_data)




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id' , 'username' , 'first_name' , 'last_name' , 'email' , 'password']

# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls , user):
#         token = super().get_token(user)
#         token['username'] = user.username
#         return token


    