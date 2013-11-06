from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
	#username associated to authenticate company
	user = models.OneToOneField(User)
	#name of the company
	name = models.CharField(max_length=20)
	#account identifier to carry our transaction handling
	account_number = models.CharField(max_length=10)
	#the phone number of the associated manager
	manager_phone = models.IntegerField()

	def __unicode__(self):
		return self.name

class BusStop(models.Model):
	#each busstop has an associated name
	name = models.CharField(max_length=30)
	def __unicode__(self):
		return self.name

class UniversalRoute(models.Model):
	#each route is uniquely identified using UniversalRoute.id
	#the starting point for each route
	source = models.ForeignKey(BusStop, related_name="route_starts")
	#the ending point for each route
	destination = models.ForeignKey(BusStop, related_name="route_ends")
	
	def __unicode__(self):
		return '%s :%s' % (self.source , self.destination)

class RouteStop(models.Model):
	#each stop can be associated to a many universal route
	route = models.ForeignKey(UniversalRoute, related_name="route_stops")
	#each entry in bus routes is a particular bus stop
	bus_stop = models.ForeignKey(BusStop)
	#stop_number on that particular universal route
	bus_stop_number = models.IntegerField()
	#distance of this particular stop on the route
	distance = models.DecimalField(max_digits=6, decimal_places=2)

	def __unicode__(self):
		return '%s:%s' % (self.bus_stop_number, self.bus_stop)

class Bus(models.Model):
	#uniquely identified using Bus.id
	#name of the bus company who owns the bus
	owner = models.ForeignKey(Company, related_name='buses')
	#the universal route number this bus travels on
	route = models.ForeignKey(UniversalRoute, related_name='buses')
	#ticket rate in rupees per kilometer
	rate = models.DecimalField(max_digits=3, decimal_places=2)
	#average speed at which this bus travels, used to calculate time of travel
	speed = models.DecimalField(max_digits=5, decimal_places=2)
	#capacity of the bus to get maximum number of allowed customers
	capacity = models.IntegerField()
	#discounts offered on this bus in percentage
	discount = models.DecimalField(max_digits=4, decimal_places=2)

	def __unicode__(self):
		return '%s ' %(self.route)


class Schedule(models.Model):
	#the bus associated with the schedule
	bus = models.ForeignKey(Bus)
	#the time of departure of the bus
	datetime = models.DateTimeField()

	def __unicode__(self):
		return '%s: %s' % ( self.bus, str(self.datetime))

class Customer(models.Model):
	#username associated with the customer
	user = models.OneToOneField(User)
	#phone number
	phone_number = models.IntegerField()
	#bank account
	account_number = models.CharField(max_length=10)
	#address
	address = models.TextField()
	#date of birth
	dob = models.DateField()
	#gender
	#gender = models.

class Transaction(models.Model):
	#identified using transaction.id
	#associated customer
	customer = models.ForeignKey(Customer)
	#associated bus from the schedule
	schedule = models.ForeignKey(Schedule)
	#amount of money spent in the transaction
	cost = models.DecimalField(max_digits=6 ,decimal_places=2)
	#seat number allocated to the user
	seat = models.IntegerField()
	#the time the transaction was created
	transaction_time = models.DateTimeField(auto_now=True)



