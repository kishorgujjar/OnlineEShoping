from django.shortcuts import render, redirect
# Create your views here.
from store.models.product import Product
from store.models.category import Category
from django.views import View


class Products(View):
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
		return redirect('products', *args, **kwargs) 


	def get(self, request, product_id):
		cart = request.session.get('cart')
		if not cart:
			request.session['cart'] = {}
		products = None
		categories = Category.get_all_categories()

		categoryID = request.GET.get('category')
		if categoryID:
			products = Product.get_all_products_by_id(categoryID)
		else:
			products = Product.objects.filter(id=product_id)
		data = {}
		data['product'] = products
		data['categories'] = categories
		return render(request, 'product.html', data)