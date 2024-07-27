from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=150)
    adress = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name + "-" + self.family + "-" + self.adress


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    img = models.ImageField(upload_to="product_img/", null=True, blank=True)

    def __str__(self):
        return self.name


class OrderApp(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    Product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.IntegerField()
    counter = models.PositiveIntegerField()
    price_all = models.BigIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Customer.name + "-" + self.Customer.family + "-" + self.Product.name + "-"
