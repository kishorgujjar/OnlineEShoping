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


class AddCart(View):
	def post(self, request , *args, **kwargs):
		product = request.POST.get('product')
		cart = request.session.get('cart')
		remove = request.POST.get('remove')

		if cart:
			quantity = cart.get(product)
			if quantity:
				if remove:
					if quantity<=1:
						cart.pop(product)
					else:
						cart[product] = quantity-1
				else:
					cart[product] = quantity+1
			else:
				cart[product] = 1
		else:
			cart = {}
			cart[product] = 1

		request.session['cart'] = cart
		return redirect('addcart', *args, **kwargs)

	def get(self, request):
		ids = list(request.session.get('cart').keys())
		products = Product.get_products_by_id(ids)
		return render(request, 'addcart.html', {'product' : products})
	
