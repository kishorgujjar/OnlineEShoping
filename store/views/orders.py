from django.shortcuts import render, redirect
# Create your views here.
from store.models.product import Product
from store.models.customer import Customer
from django.views import View
from store.models.orders import Order

from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

class OrderView(View):
	@method_decorator(auth_middleware)
	def get(self , request):
		customer = request.session.get('customer')
		order = Order.get_orders_by_customer(customer)
		return render(request , 'orders.html' , {'orders' : order})