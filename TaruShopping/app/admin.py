from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import (
    Customer,
    Product,
    Cart,
    OrderPlaced
)
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discount_price', 'description', 'brand', 'category', 'product_image']
    

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']


@admin.register(OrderPlaced)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product', "customer_info", 'quantity', 'order_date', 'status',"product_info"]


    def customer_info(self, obj):
        link = reverse('admin:app_customer_change', args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer.name)


    def product_info(self, obj):
       link = reverse('admin:app_product_change', args=[obj.product.pk])
       return format_html('<a href="{}">{}</a>', link, obj.product.title)