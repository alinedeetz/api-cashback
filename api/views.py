from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Client, Product, Order
from .serializers import CashbackSerializer, ClientSerializer, ProductSerializer, OrderSerializer

# Create your views here.

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

# class Cashback(viewsets.ModelViewSet):
#     serialier_class = CashbackSerializer