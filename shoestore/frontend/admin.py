from django.contrib import admin

# Register your models here.
from .models import Categories
from .models import Product
from .models import Customer
from .models import Order
from .models import Cart

admin.site.register(Categories)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Cart)