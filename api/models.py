from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    adress = models.CharField(max_length=50)
    email = models.EmailField(default='default@default.com')

class Product(models.Model):
    product = models.CharField(max_length=50, blank=True, null=True)
    price = models.IntegerField()


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # cashback = models.FloatField()

    @property
    def cashback(self):
        return self.product * 0.1