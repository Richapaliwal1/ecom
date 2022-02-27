from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.home_page, name="home_page"),
	path('about', views.about_page, name="about_page"),
	path('checkout', views.checkout_page, name="checkout_page"),
	path('contact', views.contact_page, name="contact_page"),
	path('icon', views.icon_page, name="icon_page"),
	path('payment', views.payment_page, name="payment_page"),
	path('product', views.product_page, name="product_page"),
	path('service', views.service_page, name="service_page"),
	path('shop', views.shop_page, name="shop_page"),
	path('single', views.single_page, name="single_page"),
	path('typography', views.typography_page, name="typography_page"),
	path('login', views.login_request, name="login_request"),
	path('register', views.register, name="register"),
	path('cart', views.cart_page, name="cart_page"),
	path('delete/<int:id>/',views.delete_data, name="deletedata"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)