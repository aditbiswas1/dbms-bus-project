from busapp.serializers import *
from busapp.forms import *
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from rest_framework import generics

from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.http import HttpResponse
from django.template import RequestContext, loader

from busapp.models import Bus, BusStop, UniversalRoute, RouteStop, Company, Customer, Transaction, Schedule


# BusStop Apis
class BusStopList(generics.ListCreateAPIView):
	"""
	Return a list of all the bustops available
	Supports Read of all the BusStops and Create for a new BusStop
	"""
	queryset = BusStop.objects.all()
	serializer_class = BusStopSerializer

class BusStopDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Return each individual BusStop
	Supports Read, Update, Destroy
	"""
	queryset = BusStop.objects.all()
	serializer_class = BusStopSerializer


#universal routes api
class UniversalRouteList(generics.ListCreateAPIView):
	queryset = UniversalRoute.objects.all()
	serializer_class = UniversalRouteSerializer

class UniversalRouteDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = UniversalRoute.objects.all()
	serializer_class = UniversalRouteSerializer

#routesStops api
class RouteStopList(generics.ListCreateAPIView):
	queryset = RouteStop.objects.all()
	serializer_class = RouteStopSerializer

class RouteStopDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = RouteStop.objects.all()
	serializer_class = RouteStopSerializer

#Base Users api
class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


#company api
class CompanyList(generics.ListCreateAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanySerializer

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanySerializer

#Bus api
class BusList(generics.ListCreateAPIView):
	queryset = Bus.objects.all()
	serializer_class = BusSerializer

class BusDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Bus.objects.all()
	serializer_class = BusSerializer

#Transaction api
class TransactionList(generics.ListCreateAPIView):
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer

class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer

#Schedule api
class ScheduleList(generics.ListCreateAPIView):
	queryset = Schedule.objects.all()
	serializer_class = ScheduleSerializer

class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Schedule.objects.all()
	serializer_class = ScheduleSerializer

#Customers api
class CustomerList(generics.ListCreateAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

def index(request):
	template = loader.get_template('index.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def customer_app(request):
	template = loader.get_template('customer_app.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def customer_app(request):
	template = loader.get_template('customer_app.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def company_app(request):
	template = loader.get_template('busapp/company_app.html')

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
			return HttpResponseRedirect('/register/success/')
	else:
		form = RegistrationForm()
		variables = RequestContext(request, {
		'form': form
		})

	return render_to_response(
	'register.html',
	variables,
	)

def register_success(request):
	return render_to_response('success.html',)
 
def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')
