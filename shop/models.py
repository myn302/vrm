from unittest.util import _MAX_LENGTH
from django.db import models
import uuid

##class 1
class Item (models.Model):
    itemID= models.AutoField
    productName =models.CharField(max_length=300, default='')
    productType= models.CharField(max_length=300, default='')
    description =models.CharField(max_length=10000, default='')
    price =models.IntegerField( default='1')
    productImage = models.ImageField(upload_to= 'Images', default='')

    def __str__(self):
        return self.productName

##class 2
class Seller (models.Model):
    sellerID= models.AutoField
    name =models.CharField(max_length=300, default='')
    email= models.CharField(max_length=300, default='')
    username=models.CharField(max_length=300, default='')
    password=models.CharField(max_length=300, default='')

    def __str__(self):
        return self.name


##class 3
class Buyer (models.Model):
    
    buyerID= models.AutoField(primary_key=True)
    itemsJson=models.CharField(max_length=300, default='')
    name =models.CharField(max_length=300, default='')
    email= models.CharField(max_length=300, default='')
    username=models.CharField(max_length=300, default='')
    password=models.CharField(max_length=300, default='')
    address= models.CharField(max_length=1000, default='')
    phone = models.CharField(max_length=1000, default='')
    payment=models.FloatField(default='1')

    def __str__(self):
        return self.name

##class 4
class Delivery(models.Model):
    deliveryID= models.AutoField(primary_key=True)
    buyerID=models.IntegerField( default='1')
    name =models.CharField(max_length=300, default='')
    date= models.DateField(default='')
    address=models.CharField(max_length=300, default='')

    def __str__(self):
        return self.name

##class 5
class Payment(models.Model):
    paymentID= models.AutoField(primary_key=True)
    deliveryID=models.IntegerField( default='1')
    cardNumber=models.CharField(max_length=300, default='')
    amount=models.FloatField(default='1')

    def __str__(self):
        return str(self.paymentID)



