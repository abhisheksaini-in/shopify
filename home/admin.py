from django.contrib import admin
from home.models import Product, Cart, OrderPlaced, Customer

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'discount_price', 'brand')
    list_filter = ('category',)
    search_fields = ('title',)
    
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'status', 'quantity')
    search_fields = ('user','product')
    
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product',  'quantity')
    search_fields = ('user',)
    
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','user','zipcode','Address', 'state')
    search_fields = ('name', 'zipcode')
    list_per_page = 15
    

admin.site.register(Product, ProductAdmin)
admin.site.register(OrderPlaced, OrderPlacedAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Cart, CartAdmin)
