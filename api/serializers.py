from rest_framework import routers, serializers, viewsets
from .models import Client, Product, Order



class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'adress', 'email')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'client', 'product', 'qty', 'cashback']

class CashbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'