from django.shortcuts import render
from django.shortcuts import render
from importlib_metadata import metadata
from rest_framework import status
from rest_framework.response import Response
from sales.models import OrderProduct
from sales.models import Product
from sales.models import Order
 
from rest_framework.decorators import api_view

from django.views.decorators.csrf import csrf_exempt
import stripe

stripe.api_key = 'sk_test_51Kpr85DP9ndu4EFOTqCLn00O0N9U5V5FLyval6cPXhilZxUWnop4ujWv7JmNsxqcFEGwrScGPxuJCDhuk6LIp0QJ00e8oSFWOl'

@csrf_exempt
@api_view(['POST'])
def create_payment(request):
    data = request.data
    email = data['email']
    items = data['items']
    total = float(data['delivery_charges'])
    order = Order(
        email = email,
        last_name = data['last_name'],
        first_name = data['first_name'],
        phone_number = data['phone_number'],
        address = data['address'],
        postal_code = data['postal_code'],
        country = data['country'],
        town = data['town'],
        delivery_charges = float(data['delivery_charges']),
        total = total,
        user = request.user
    )
    order.save()
    for item in items:
        product = Product.objects.get(pk=item['id'])
        orderProduct = OrderProduct(
            product=product, 
            label=item['label'], 
            price = float(item['price']), 
            quantity=float(item['quantity']), 
            order = order,
            image_url = item['image']
        )
        orderProduct.save()
        #reduce quantity
        product.qte_stock = float(product.qte_stock) - float(item['quantity'])
        product.save()
        total += float(item['quantity']) * float(item['price'])
    order.total = total
    order.save()
    #create order
    payment_intent = stripe.PaymentIntent.create(
        amount=int(total * 100), 
        currency='eur', 
        payment_method_types=['card'],
        receipt_email=email,
    )
    return Response(status=status.HTTP_200_OK, data={'payment_intent': payment_intent})