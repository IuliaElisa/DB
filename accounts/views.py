from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail, BadHeaderError
from django.views.generic import ListView


# Create your views here.
from .models import *
from .forms import OrderForm, CreateUserForm, ObjectForm, ContribForm, ArticleForm
from .filters import OrderFilter

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)


class SearchResultsView(ListView):
    model = Object
    template_name = "search_results.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Object.objects.filter(
            Q(name__icontains=query)
        )
        return object_list

def redirect_view(request):
    response = redirect('jolie-home.html')
    return render(request, 'accounts/jolie-home.html')

def redirect_plannets(request):
    response = redirect('planete.html')
    return render(request, 'accounts/planete.html')
	
def redirect_corps(request):
    response = redirect('corps.html')
    return render(request, 'accounts/corps.html')
	
def redirect_varsta(request):
    response = redirect('varsta.html')
    return render(request, 'accounts/varsta.html')

def redirect_lumin(request):
    response = redirect('lumin.html')
    return render(request, 'accounts/lumin.html')

def redirect_gravity(request):
    response = redirect('viteze.html')
    return render(request, 'accounts/viteze.html')

def redirect_contact(request):
    response = redirect('contact.php')
    return render(request, 'accounts/contact.php')

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()

	total_customers = customers.count()
	objects = Object.objects.all();
	contributors = Contributor.objects.all();

	total_orders = orders.count()
	total_objects = objects.count()

	#delivered = orders.filter(status='Done').count()
	mb = objects.filter(tags='Main-Belt').count()
	neo = objects.filter(category = 'NEO').count()

	context = {'objects':objects, 'contributors':contributors,
	'total_contributions':total_objects, 'category':neo, 'main_belt':mb}

	return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def products(request):
	products = Product.objects.all()

	return render(request, 'accounts/products.html', {'products':products})

@login_required(login_url='login')
def object(request):
	objectt = Object.objects.all()

	return render(request, 'accounts/objects.html', {'objects':objectt})

def article(request):
	articles = Article.objects.all()
	return render(request, 'accounts/articles.html', {'articles':articles})


@login_required(login_url='login')
def contributor(request, pk_test):
	contributors = Contributor.objects.all();

	'''
	orders = contributor.order_set.all()
	order_count = orders.count()

	myFilter = OrderFilter(request.GET, queryset=orders)
	orders = myFilter.qs 

	context = {'customer':customer, 'orders':orders, 'order_count':order_count,
	'myFilter':myFilter}
	'''
	return render(request, 'accounts/contributor.html',{'contributors':contributors})

@login_required(login_url='login')
def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()

	myFilter = OrderFilter(request.GET, queryset=orders)
	orders = myFilter.qs 

	context = {'customer':customer, 'orders':orders, 'order_count':order_count,
	'myFilter':myFilter}
	return render(request, 'accounts/customer.html',context)

@login_required(login_url='login')
def createOrder(request, pk):
	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10 )
	customer = Customer.objects.get(id=pk)
	formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
	form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		formset = OrderFormSet(request.POST, instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('/')

	context = {'form':formset}
	return render(request, 'accounts/order_form.html', context)


@login_required(login_url='login')
def addObject(request):
	form = ObjectForm()
	if request.method == 'POST':
		#print('Print',request.POST)
		form = ObjectForm(request.POST)
		if form.is_valid():
				form.save()
				return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/add_object.html', context)


@login_required(login_url='login')
def addContributor(request):
	form = ContribForm()
	if request.method == 'POST':
		#print('Print',request.POST)
		form = ContribForm(request.POST)
		if form.is_valid():
				form.save()
				return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/add_contributor.html', context)

@login_required(login_url='login')
def addArticle(request):
	form = ArticleForm()
	if request.method == 'POST':
		#print('Print',request.POST)
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/add_article.html', context)




@login_required(login_url='login')
def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'accounts/delete.html', context)