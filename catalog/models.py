from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s provider" % self.name


class City(models.Model):
    provider = models.OneToOneField(Provider, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return "%s city" % self.name


class Product(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s product" % self.name


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=80)
    email = models.EmailField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

