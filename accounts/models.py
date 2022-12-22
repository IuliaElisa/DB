from django.db import models
from django_quill.fields import QuillField
from django.utils import timezone
# Create your models here.


class Article(models.Model):
		name = models.CharField(max_length = 50)
		content = QuillField(default = '')
		title = models.CharField(max_length=255)
		title_tag = models.CharField(max_length=255)
		author = models.CharField(max_length=50, null=True)
		post_date = models.DateField(default=timezone.now)
		
		def __str__(self):
			return self.name


class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Contributor(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('In progress', 'In progress'),
			('Done', 'Done'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=1000, null=True)

	def __str__(self):
		return self.product.name




class Object(models.Model):
	CATEGORY = (
			('NEO', 'NEO'),
			('Non-NEO', 'Non-NEO'),
			)
	TAGS = (
			('Main-Belt', 'Main-Belt'),
			('AMO', 'AMO'),
			('APO', 'APO'),
			('ATE', 'ATE'),
			)  
	contributor = models.CharField(max_length=50, null=True)
	name = models.CharField(max_length=200, null=True)
	magnitude = models.FloatField(null=True)
	diameter = models.FloatField(null=True)
	mass = models.FloatField(null=True)
	perihelion = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=2000, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.CharField(max_length=200, null=True, choices=TAGS)

	def __str__(self):
		return self.name

