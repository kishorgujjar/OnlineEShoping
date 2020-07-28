from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View

class Signup(View):
	def get(self , request):
		return render(request, 'signup.html')

	def post(self , request):
		postData = request.POST
		first_name = postData.get('firstname')
		last_name = postData.get('lastname')
		phone = postData.get('phone')
		email = postData.get('email')
		password = postData.get('password')

		# validation
		value = {
			'first_name' : first_name,
			'last_name' : last_name,
			'phone' : phone,
			'email' : email
		}

		error_message = None
		customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
		error_message = self.validateCustomer(customer)
		
		if not error_message:
			customer.password = make_password(customer.password)
			customer.register()
			return redirect('index')
		else:
			data = {
				'error' : error_message,
				'values' : value
			}
			return render(request, 'signup.html', data)

	def validateCustomer(self , customer):
		error_message = None
		if(not customer.first_name):
			error_message = "First Name Requred !!"
		elif len(customer.first_name) < 4:
			error_message = "First name must be 4 character long or more"
		elif not customer.last_name:
			error_message = "Last name required"
		elif len(customer.last_name) < 4:
			error_message = "Last name must be 4 character long or more"
		elif not customer.phone:
			error_message = "Phone number required"
		elif len(customer.phone) < 10:
			error_message = "phone number must be 10 char long"
		elif len(customer.email) < 6:
			error_message = "Email must be 6 character long"
		elif len(customer.password) < 6:
			error_message = "Password must be 6 character long"
		elif customer.isExist():
			error_message = 'Email Address Already Registered'

		return error_message