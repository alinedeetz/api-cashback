from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    phone = models.CharField(max_length=50, null=True)
    REQUIRED_FIELDS = ['username', 'phone', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email

class Client(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    document = models.CharField(max_length=11)
    address = models.CharField(max_length=50)
    email = models.EmailField(default='default@default.com')


class Product(models.Model):
    product = models.CharField(max_length=50, blank=True, null=True)
    price = models.IntegerField()


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()

    @property
    def cashback(self):
        valor_total = self.product.price * self.qty
        return valor_total * 0.1

class CashbackResponse(models.Model):
    response = models.CharField(max_length=256)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
