from busapp.serializers import *
from busapp.forms import *
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.http import HttpResponse
from django.template import RequestContext, loader

from busapp.models import Bus, BusStop, UniversalRoute, RouteStop, Company, Customer, Transaction, Schedule
from busapp.permissions import *

# BusStop Apis
class BusStopList(generics.ListCreateAPIView):
	"""
	Return a list of all the bustops available
	Supports Read of all the BusStops and Create for a new BusStop
	"""
	#permission_classes = 3
	queryset = BusStop.objects.all()
	serializer_class = BusStopSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsCompanyUser_or_Admin_or_ReadOnly,)

class BusStopDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Return each individual BusStop
	Supports Read, Update, Destroy
	"""
	#permission_classes = 1
	queryset = BusStop.objects.all()
	serializer_class = BusStopSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAdmin_or_ReadOnly,)

#universal routes api
class UniversalRouteList(generics.ListCreateAPIView):
        #permission_classes = 3
	queryset = UniversalRoute.objects.all()
	serializer_class = UniversalRouteSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCompanyUser_or_Admin_or_ReadOnly,)

class UniversalRouteDetail(generics.RetrieveUpdateDestroyAPIView):
        #permission_classes = 1
	queryset = UniversalRoute.objects.all()
	serializer_class = UniversalRouteSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAdmin_or_ReadOnly,)

#routesStops api
class RouteStopList(generics.ListCreateAPIView):
        #permission_classes = 3
	queryset = RouteStop.objects.all()
	serializer_class = RouteStopSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCompanyUser_or_Admin_or_ReadOnly,)

class RouteStopDetail(generics.RetrieveUpdateDestroyAPIView):
        #permission_classes = 1
	queryset = RouteStop.objects.all()
	serializer_class = RouteStopSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAdmin_or_ReadOnly,)

#Base Users api
class UserList(generics.ListCreateAPIView):
        #permission_classes = 4
	queryset = User.objects.all()
	serializer_class = UserSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAdmin,)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
        #permission_classes = 5
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsUser,)


#company api
class CompanyList(generics.ListCreateAPIView):
        #permission_classes = 3
	queryset = Company.objects.all()
	serializer_class = CompanySerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCompanyUser_or_Admin_or_ReadOnly,)
        def pre_save(self,obj):
                obj.owner = self.request.user

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
        #permission_classes = 6
	queryset = Company.objects.all()
	serializer_class = CompanySerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCompany,)
	def pre_save(self,obj):
                obj.owner = self.request.user

#Bus api
class BusList(generics.ListCreateAPIView):
        #permission_classes = 2
	queryset = Bus.objects.all()
	serializer_class = BusSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCompanyUser_or_ReadOnly,)
	def pre_save(self, obj):
                obj.owner = self.request.owner

class BusDetail(generics.RetrieveUpdateDestroyAPIView):
        #permission_classes = 11 (change it)
	queryset = Bus.objects.all()
	serializer_class = BusSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCompanyUser_or_ReadOnly_11,)
	def pre_save(self, obj):
                obj.owner = self.request.owner

#Transaction api
class TransactionList(generics.ListCreateAPIView):
        #permission_classes = 7
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IfCustomer,)

	def pre_save(self, obj):
                obj.owner = self.request.customer

class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
        #permission_classes = 8
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsRequest_or_isSafeOnlyMethod,)

	def pre_save(self, obj):
                obj.owner = self.request.customer

#Schedule api
class ScheduleList(generics.ListCreateAPIView):
        #permission_classes = 2
	queryset = Schedule.objects.all()
	serializer_class = ScheduleSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCompanyUser_or_ReadOnly,)
        
class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
        #permission_classes = 2
	queryset = Schedule.objects.all()
	serializer_class = ScheduleSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCompanyUser_or_ReadOnly,)

#Customers api
class CustomerList(generics.ListCreateAPIView):
        #permission_classes = 9
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsAdmin_or_Customer,)
	
        def pre_save(self,obj):
                obj.owner = self.request.user

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
        #permission_classes = 10
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsCustomer,)
	
        def pre_save(self,obj):
                obj.owner = self.request.user

def index(request):
	template = loader.get_template('index.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def customer_app(request):
	template = loader.get_template('customer_app.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def company_app(request):
	template = loader.get_template('busapp/company_app.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def customer_confirm(request):
	template = loader.get_template('customer_seats.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))
	
@csrf_protect
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
			username=form.cleaned_data['username'],
			password=form.cleaned_data['password1'],
			email=form.cleaned_data['email']
			)
			choice=form.cleaned_data['choice_field']
			if choice=='1':
				return HttpResponseRedirect('/register/company/'+user.username)
			else:
				return HttpResponseRedirect('/register/customer/'+user.username)
		else:
			variables = RequestContext(request, {
			'form': form
			})	
	else:
		form = RegistrationForm()
		variables = RequestContext(request, {
		'form': form
		})		

	return render_to_response(
	'register.html',
	variables,
	)
	
def regcustomer(request,url):
	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			g=''
			if form.cleaned_data['gender']=='1':
				g='Male'
			else:
				g='Female'
			customer = Customer.objects.create(
			user=User.objects.filter(username=url.split('/')[0])[0],
			fname=form.cleaned_data['fname'],
			lname=form.cleaned_data['lname'],
			phone_number=form.cleaned_data['phone'],
			account_number=form.cleaned_data['bank'],
			address=form.cleaned_data['address'],
			dob=form.cleaned_data['dob'],
			gender=g
			)
			#customer.save()
			return HttpResponseRedirect('/register/success/')
		else:
			variables = RequestContext(request, {
			'form': form
			})
	else:
		form = CustomerForm()
		variables = RequestContext(request, {
		'form': form
		})		

	return render_to_response(
	'regcustomer.html',
	variables,
	)
	
def regcompany(request,url):
	if request.method == 'POST':
		form = CompanyForm(request.POST)
		if form.is_valid():
			company = Company.objects.create(
			user=User.objects.filter(username=url.split('/')[0])[0],
			name=form.cleaned_data['name'],
			account_number=form.cleaned_data['account_number'],
			manager_phone=form.cleaned_data['manager_phone']
			)
			return HttpResponseRedirect('/register/success/')
		else:
			variables = RequestContext(request, {
			'form': form
			})
	else:
		form = CompanyForm()
		variables = RequestContext(request, {
		'form': form
		})		

	return render_to_response(
	'regcompany.html',
	variables,
	)

def register_success(request):
	return render_to_response('success.html',)

def redirect_to_app(request):
	user = User.objects.get(username=request.user)
	try:
		company = user.company
	except:
		company = None
	try:
		customer = user.customer
	except:
		customer = None
	
	if company != None:
		return HttpResponseRedirect('/company-app/')
	elif customer != None:
		return HttpResponseRedirect('/customer-app/')

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')
