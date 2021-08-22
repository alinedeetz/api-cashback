from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    adress = models.CharField(max_length=50)
    email = models.EmailField(default='default@default.com')
