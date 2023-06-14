from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=1000000)
    sizes = models.CharField(max_length=100)
    price = models.FloatField()
    rate = models.FloatField()
    rate_text = models.CharField(max_length=5,default='FFFFF')
    featured_product = models.BooleanField(default=False)
    offer = models.BooleanField(default=False)
    image = models.ImageField(upload_to='static/images/',blank=True, null=True)
    gallery_1 = models.ImageField(upload_to='static/images/',blank=True, null=True)
    gallery_2 = models.ImageField(upload_to='static/images/',blank=True, null=True)
    gallery_3 = models.ImageField(upload_to='static/images/',blank=True, null=True)
    gallery_4 = models.ImageField(upload_to='static/images/',blank=True, null=True)
    offer_image = models.ImageField(upload_to='static/images/',blank=True, null=True)

class testimonial(models.Model):
    name = models.CharField(max_length=500)
    comment = models.CharField(default="this is from django default comment elit. Quis, repellat. Id natus aut, quasi unde voluptatum, ipsa fugit esse enim numquam officiis cupiditate repellendus nihil fuga. A iure fugit hic. lo",max_length=1000000)
    rate_text = models.CharField(max_length=5,default='FFFFF')
    image = models.ImageField(upload_to='static/images/',blank=True, null=True)

class order(models.Model):
    username = models.CharField(max_length=500)
    product = models.ForeignKey(product, default=None, on_delete=models.CASCADE)
    size = models.CharField(max_length=100)
    count = models.IntegerField()
    is_confirmed = models.BooleanField(default=False)

class confirmed_orders(models.Model):
    user = models.ForeignKey(User,default=None, on_delete=models.CASCADE)
    address = models.CharField(max_length=100000, default="")
    phone = models.CharField(max_length=15, default="")
    total_price = models.FloatField()
