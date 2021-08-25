from rest_framework import routers, serializers, viewsets
from .models import *
from djoser.serializers import UserCreateSerializer, UserSerializer

class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('__all__')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        
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

class CashbackResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashbackResponse
        fields = '__all__'