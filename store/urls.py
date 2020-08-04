from django.contrib import admin
from django.urls import path
from .views.home import Index 
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart , AddCart
from .views.checkout import CheckOut 
from .views.orders import OrderView
from .views.shop import Shop
from .views.products import Products



urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('signup/', Signup.as_view() , name='signup'),
    path('login/', Login.as_view() , name='login'),
    path('logout/', logout , name='logout'),
    path('cart/', Cart.as_view() , name='cart'),
    path('check-out/', CheckOut.as_view() , name='checkout'),
    path('orders/', OrderView.as_view() , name='orders'),
    path('shop/', Shop.as_view() , name='shop'),
    path('products/<product_id>/', Products.as_view() , name='products'),

    path('addcart/', AddCart.as_view() , name='addcart'),

]
