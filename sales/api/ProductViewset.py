from cProfile import label
from functools import reduce
import json
from numpy import product
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from sales.models import Image
from sales.models import Product, VariantType
from sales.serializers import ProductSerializer, CreateProductSerializer, VariantTypeSerializer, ImageSerializer
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import operator

class ProductViewset(ModelViewSet):
    serializer_class = ProductSerializer
    create_serializer_class = CreateProductSerializer
    def get_queryset(self):
        queryset = Product.objects
        category_id = self.request.GET.get('category')
        if category_id is not None:
            queryset = queryset.filter(category__id=category_id)
        is_variant = self.request.GET.get('is_variant')
        if is_variant is not None:
            queryset = queryset.filter(is_variant=is_variant)
        search_text = self.request.GET.get('search_text')
        if search_text is not None:
            list = search_text.split()
            queryset = queryset.filter(reduce(operator.or_, ((Q(label__contains=x) | Q(description__contains=x)) for x in list)))
        return queryset

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update" or self.action == "partial_update":
            return self.create_serializer_class
        return super().get_serializer_class()

class ImageViewset(ModelViewSet):
    serializer_class = ImageSerializer
    def get_queryset(self):
        return Image.objects.all()
    
    @action(detail=True, methods=['put'], url_path="remove")
    def remove(self, request, pk):
        image = self.get_object()
        image.delete()
        return Response(image)
        


class VariantTypeViewset(ModelViewSet):
    serializer_class = VariantTypeSerializer
    def get_queryset(self):
        return VariantType.objects.all()
