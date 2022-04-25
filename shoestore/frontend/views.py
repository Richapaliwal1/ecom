from django.http import HttpResponse
from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.forms import UserCreationForm
from .models import Product
from .models import Cart
from .models import Customer	
import razorpay							
# Create your views here.

def home_page(request):
	return render(request, "index.html", context={})

def about_page(request):
	return render(request, "about.html", context={})

def cart_page(request):
	login_user = request.user
	if not login_user.is_authenticated:
		return JsonResponse({'status':False, 'msg':"User is not logged In!"})
	allcart = Cart.objects.all()
	detail = Customer.objects.all()
	mycart = Cart.objects.filter(user=login_user, is_active=True)
	total = 0
	for i in mycart:
		total += (i.quantity*i.product.price)
	return render(request, "checkout.html", {'mycart':mycart, 'total':total, 'allcart':allcart, "detail":detail})

def delete_data(request,id):
	if request.method == 'POST':
		pi = Cart.objects.get(pk=id)
		pi.delete()
		return render(request,'checkout.html')
def checkout_page(request):
	if request.method == "POST":
		cart = Cart(product_name=request.POST['product_name'], price=request.POST['price'], image=request.POST['image'])
		cart.save()
	return render(request,'checkout.html')

def contact_page(request):
	return render(request, "contact.html", context={})	

def icon_page(request):
	return render(request, "icon.html", context={})	

def payment_page(request):
	# if request.method == 'GET':
	client = razorpay.Client(auth=("rzp_test_Tve6FawTIgxnWU", "AqXKVHo3TrRdUtjkFWvoGsn0"))
	price= request.GET.get('total')
	DATA = {
		"amount"  : price,
		"currency": "INR",
	}

	client.order.create(data=DATA)
	return render(request, "payment.html", {'price' : price})	

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
	return render(request, "typography.html", context={})

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


from django.http import JsonResponse

def addToCart(request):
	login_user = request.user
	product_id = request.GET.get('product_id')

	if not login_user.is_authenticated:
		return JsonResponse({'status':False, 'msg':"User is not logged In!"})
	if not product_id:
		return JsonResponse({'status':False, 'msg':"Please send product id!"})
	
	product = Product.objects.get(id=product_id)

	if Cart.objects.filter(product=product, user=login_user, is_active=True).exists():
		cart = Cart.objects.filter(product=product, user=login_user, is_active=True).last()
		cart.quantity += 1
		cart.save()
	else:
		cart = Cart.objects.create(product=product, user=login_user)
	return JsonResponse({'status':True, 'msg':"Item added successfully!", 'cart_id':cart.id})


def cust_details(request):
	if request.method=='POST':
		cust_name=request.POST['cust_name']
		email=request.POST['email']
		address=request.POST['address']
		phone=request.POST['phone']
		cust=Customer.objects.create(cust_name=cust_name,email=email,address=address,phone=phone)
		messages.success(request,'Data has been submitted')
	return render(request,'payment.html')

def details(request):
	
	return render(request, "payment.html", {'detail':detail})	