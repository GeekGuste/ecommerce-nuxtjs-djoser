from django.shortcuts import render
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from sales.models import Category
from sales.serializers import CategorySerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def categorie_list(request):
    #zsefe
 
@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    # find category by pk (id)
    try: 
        categorie = Category.objects.get(pk=pk) 
    except Category.DoesNotExist: 
        return JsonResponse({'message': 'The category does not exist'}, status=status.HTTP_404_NOT_FOUND) 
