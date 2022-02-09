
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from tinymce.models import HTMLField

# Create your models here.
# password = store

STATE_CHOICE = (
        ('Uttar Pradesh','Uttar Pradesh'),
        ('Madhya Pradesh','Madhya Pradesh'),
        ('Andhra Pradesh','Andhra Pradesh'),
        ('Assam','Assam'),
        ('Gujarat','Gujarat'),
        ('Bihar','Bihar'),
        ('Mumbai','Mumbai'),
        ('Arunachal','Arunachal'),
        ('Jammu & Kashmir','Jammu & Kashmir'),
        ('Uttrakhand','Uttrakhand'),
        ('Karnatka','Karnatka'),
        ('Haryana','Haryana'),
        ('Goa','Goa'),
    )

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    Address = models.CharField(max_length=500)
    phone = models.CharField(max_length=15, null=False, default=000000000)
    city = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    state = models.CharField(choices = STATE_CHOICE, max_length=100)
    country = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.id)
    
    
CATEGORY_CHOICE = (
    ('MB', 'Mobile'),
    ('AP', 'Appliances'),
    ('MF', 'Men Fashion'),
    ('WF', 'Women Fashion'),
    ('MFW', 'Men Footwear'),
    ('WFW', 'Women Footwear'),
)
    
    
    
class Product(models.Model):
    title = models.CharField(max_length=400)
    url = models.SlugField()
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=100)
    brand = models.CharField(max_length=400)
    selling_price = models.FloatField(max_length=10)
    discount_price = models.FloatField(max_length=10)
    discount_percent = models.FloatField(max_length=10)
    product_desc = HTMLField()
    offer_detail = HTMLField()
    image = models.ImageField(upload_to = 'ProductImage/')
    add_time = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title
    
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
    
STATUS_CHOICE = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(choices=STATUS_CHOICE, max_length=100, default= 'Pending' )
    
    def __str__(self):
        return self.user
    
    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price
    
 
