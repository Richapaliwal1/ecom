
from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.forms import UserCreationForm
from .models import Product
# Create your views here.

def home_page(request):
	return render(request, "index.html", context={})

def about_page(request):
	return render(request, "about.html", context={})

def checkout_page(request):
	product_name = request.GET['product_name']
	price = request.GET['Price']
	image = request.GET['image']
	context = {
	'product_name':product_name,
	'price':price,
	'image':image,

	}
	return render(request, "checkout.html", context)

def contact_page(request):
	return render(request, "contact.html", context={})	

def icon_page(request):
	return render(request, "icon.html", context={})	

def payment_page(request):
	return render(request, "payment.html", context={})	

def product_page(request):
	return render(request, "product.html", context={})	

def service_page(request):
	return render(request, "service.html", context={})		

def shop_page(request):
	data = Product.objects.all()
	return render(request, "shop.html",{'data':data})	

def single_page(request):
	return render(request, "single.html", context={})	

def typography_page(request):
	return render(request, "typograph.html", context={})

def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("register")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = UserCreationForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login_page.html", context={"login_form":form})

							