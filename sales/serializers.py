from dataclasses import field
from pyexpat import model
import this
from unicodedata import category
from matplotlib.pyplot import cla
from rest_framework import serializers
from sales.models import Image
from sales.models import VariantType
from sales.models import Product 
from sales.models import Category
 
 
class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField()
    class Meta:
        model = Category
        #fields = '__all__'
        fields = ('id',
                  'label',
                  'is_active',
                  'parent')
    def get_parent(self, instance):
        if instance.parent is not None:
            return CategorySerializer(instance.parent).data
        else:
            return None


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id',
                  'label',
                  'is_active',
                  'parent')

class CategoryTreeSerializer(serializers.ModelSerializer):
    enfants = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ('id',
                  'label',
                  'is_active',
                  'enfants')
    
    def get_enfants(self, instance):
        queryset = instance.enfants.all()
        return CategoryTreeSerializer(queryset, many=True).data


class VariantTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariantType
        fields = ('id',
                 'label')

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id',
                  'category',
                  'label',
                  'parent',
                  'description',
                  'qte_stock',
                  'principal_image',
                  'price',
                  'promo_price',
                  'is_variant',
                  'variant_type',
                  'variant_value',
                  'is_active')

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id',
                  'photo',
                  'product')

class ProductVariantSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = Product
        fields = ('id',
                  'category',
                  'variant_type',
                  'variant_value',
                  'label',
                  'images',
                  'description',
                  'qte_stock',
                  'principal_image',
                  'is_variant',
                  'price',
                  'is_variant',
                  'promo_price',
                  'pub_date')



class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)
    variant_type = VariantTypeSerializer(many=False)
    parent = serializers.SerializerMethodField()
    variants = ProductVariantSerializer(many=True)
    images = ImageSerializer(many=True)
    class Meta:
        model = Product
        fields = ('id',
                  'category',
                  'variant_type',
                  'variant_value',
                  'parent',
                  'images',
                  'variant_type',
                  'variants',
                  'label',
                  'description',
                  'qte_stock',
                  'principal_image',
                  'is_variant',
                  'price',
                  'is_variant',
                  'promo_price',
                  'pub_date')
    def get_parent(self, instance):
        if instance.parent is not None:
            return ProductSerializer(instance.parent).data
        else:
            return None
    def get_variants(self, instance):
        queryset = instance.variants.all()
        return ProductVariantSerializer(queryset, many=True).data
