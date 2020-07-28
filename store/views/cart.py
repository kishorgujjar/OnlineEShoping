from django.shortcuts import render, redirect
# Create your views here.

from store.models.product import Product
from store.models.customer import Customer
from django.views import View

from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator


class Cart(View):
	@method_decorator(auth_middleware)
	def get(self , request):
		ids = list(request.session.get('cart').keys())
		products = Product.get_products_by_id(ids)
		return render(request, 'cart.html', {'product' : products})

	