from django.db import models
import datetime
from django.views import View
from django.contrib.auth.models import User

# Create your models here.

class Categories(models.Model):
	name = models.CharField(max_length=120)
	
	def __str__(self):
		return self.name

class Customer(models.Model):
	cust_name = models.CharField(max_length=120)
	email = models.EmailField(max_length=120)
	address = models.CharField(max_length=120)
	phone = models.CharField(max_length=10)
	

	def __str__(self):
		return self.cust_name

class Product(models.Model):
	product_name = models.CharField(max_length=120)
	price = models.IntegerField()
	category = models.ForeignKey(Categories, on_delete=models.CASCADE)
	description = models.CharField(max_length=250, default='')
	image = models.ImageField(upload_to='media/')
	
	def __str__(self):
		return self.product_name
	

class Order(models.Model):
	product = models.ForeignKey(Product,
								on_delete=models.CASCADE)
	customer = models.ForeignKey(Customer,
								 on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	price = models.IntegerField()
	address = models.CharField(max_length=50, default='', blank=True)
	phone = models.CharField(max_length=10, default='', blank=True)
	date = models.DateField(default=datetime.datetime.today)
	status = models.BooleanField(default=False)

	def placeOrder(self):
		self.save()

class Cart(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField(auto_now_add=True)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.product.product_name



	# product_name = models.CharField(max_length=120)
	# price = models.IntegerField()
	# image = models.ImageField(upload_to='media/')
	
	# def __str__(self):
	# 	return self.product_name
	



