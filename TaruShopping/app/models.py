from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.

STATE_CHOICES = (
    ('Afg', ' Afganistan'),
    ('Brz', 'Brazil'),
    ('Comb', "Combodia"),
    ('Canada', "Canada"),
    ('Eng', 'England'),
    ('Europe', 'Europe'),
    ('Florida', 'Florida'),
    ('Ind', 'India'),
    ('Jarisuelum', "jarisuelum"),
    ('Labanon', "Labanon"),
    ('Mongolia', "Mongolia"),
    ('Malta', "Malta"),
    ('Nepal', 'Nepal'),
    ('Oman', 'Oman'),
    ('Pak', 'Pakistan'),
    ('Qatar', 'Qatar'),
    ('Saudi Arabia', 'Saudi Arabia'),
    ('Uzbakistan', 'Uzbakistan'),

)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    state = models.CharField(choices = STATE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES = (
    ('M', 'Mobile'),
    ('L', 'Lapetop'),
    ('TW', 'Top Wear'),
    ('BW', 'Bottom Wear'),
    ('S', "Shoes")
)

class Product(models.Model):
    title = models.CharField(max_length=30)
    selling_price = models.FloatField()
    discount_price = models.FloatField()    
    description = models.TextField()
    brand = models.CharField(max_length=40)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    product_image = models.ImageField(upload_to='productimg')
    

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price

STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On the way', 'On the way'),
    ('Cancel', 'Cancel')
)
class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer =  models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price