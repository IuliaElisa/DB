from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



from .models import Order, Object, Contributor, Article


class ObjectForm(ModelForm):
	class Meta:
			model = Object
			fields = '__all__'

class ContribForm(ModelForm):
	class Meta:
		model = Contributor
		fields = '__all__'

class ArticleForm(ModelForm):
	class Meta:
		model = Article
		fields = '__all__'

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
