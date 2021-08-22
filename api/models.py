from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    document = models.CharField(max_length=11)
    adress = models.CharField(max_length=50)
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