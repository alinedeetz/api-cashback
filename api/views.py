from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Client, Product, Order
from .serializers import CashbackSerializer, ClientSerializer, ProductSerializer, OrderSerializer
import requests

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

    @action(detail=True, methods=['post'])
    def cashback(self, request, pk=None):
        order = self.get_object()
        document = order.client.document
        cashback = order.cashback
        url = 'https://5efb30ac80d8170016f7613d.mockapi.io/api/mock/Cashback'
        data = {
            'document': document,
            'cashback': cashback
        }
        r = requests.post(url, data=data)
        if r.status_code == 200:
            response = Response({'status': 'Cashback requested successfully'})
        else:
            response = Response({'status': 'Error while requesting cashback', 'error': r.text}, status=500)
        return response