from django.shortcuts import render, redirect
# Create your views here.
from store.models.product import Product
from store.models.category import Category
from django.views import View


class Shop(View):
	def post(self , request):
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
		return redirect('shop')


	def get(self , request):
		cart = request.session.get('cart')
		if not cart:
			request.session['cart'] = {}
		products = None
		categories = Category.get_all_categories()

		categoryID = request.GET.get('category')
		if categoryID:
			products = Product.get_all_products_by_id(categoryID)
		else:
			products = Product.get_all_products()

		data = {}
		data['product'] = products
		data['categories'] = categories
		return render(request, 'shop.html', data)
	
