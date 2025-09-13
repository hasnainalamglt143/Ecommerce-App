from django.db import models
from . import validators

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    phone=models.CharField(max_length=15, unique=True,validators=[validators.validatePhone])

    class Meta:
        verbose_name_plural = "Customers"



    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    name=models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True,default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='category',default=1)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name


class Order(models.Model):
    status_choices = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending',choices=status_choices)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.TextField()

    class Meta:
        verbose_name_plural = "Orders"
    
    def __str__(self):
        return f"Order {self.id} - {self.product.name} for {self.customer.first_name}"


