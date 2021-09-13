from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

Division_Choice = (
    ("Dhaka","Dhaka"),
    ("Khulna","Khulna"),
    ("Rajshahi","Rajshahi"),
    ("Chattrogram", "Chattrogram"),
    ("Mymansin","Mymansin")
    )

city_choice =(
    ("Dhaka","Dhaka"),
    ("Tangail","Tangail"),
    ("Gazipur","Gazipur"),
    ("Rajshahi","Rajshahi"),
    ("Chattrogram", "Chattrogram"),
    ("Mymansin","Mymansin")
    ) 

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    Division_Choice= models.CharField(choices=Division_Choice, max_length=200)
    city = models.CharField(choices=city_choice,max_length=200)
    zipcode = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES = (
    ("M","Mobile"),
    ("L", "Laptop"),
    ("TW","Top Wear"),
    ("BW","Bottom Wear")
)

class Product(models.Model):
    title = models.CharField(max_length=200)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    Product_image = models.ImageField(upload_to = 'product_img')

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)


STATUS_CHOICES = (
    ("Confirm","Confirm"),
    ("Processing","Processing"),
    ("Pick","Pick"),
    ("Shipped","Shipped"),
    ("Delivered","Delivered"),
    ("Cancel","Cancel")
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES,default='pending', max_length=100)



