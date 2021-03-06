from rest_framework import serializers
from busapp.models import BusStop, UniversalRoute, RouteStop, Company, Bus, Transaction, Schedule, Customer
from django.contrib.auth.models import User
#serializer class for busstops
class BusStopSerializer(serializers.ModelSerializer):
	class Meta:
		model = BusStop
		fields = ('id', 'name')


#serialize users
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username')



#serialize universal routes
class UniversalRouteSerializer(serializers.ModelSerializer):
	route_stops = serializers.HyperlinkedRelatedField(read_only=True, view_name="routestop-detail")
	source = BusStopSerializer()
	destination = BusStopSerializer()
	class Meta:
		model = UniversalRoute
		fields = ('id', 'source', 'destination', 'route_stops')

#serialize route stops
class RouteStopSerializer(serializers.ModelSerializer):
	route = UniversalRouteSerializer()
	bus_stop = BusStopSerializer()
	class Meta:
		model = RouteStop
		fields = ('id', 'route', 'bus_stop', 'bus_stop_number', 'distance')

#serialize company
class CompanySerializer(serializers.ModelSerializer):
	user = serializers.PrimaryKeyRelatedField(read_only=True)
	buses = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="bus-detail")
	class Meta:
		model = Company
		fields = ('id', 'user', 'name', 'manager_phone', 'buses')
		

class BusSerializer(serializers.ModelSerializer):
	"""
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
	"""
	owner = CompanySerializer()
	route = UniversalRouteSerializer()
	class Meta:
		model = Bus
		fields = ('id', 'owner', 'route', 'rate', 'speed', 'capacity', 'discount')
		read_only_field = ('owner',)


class CompanySerializer(serializers.ModelSerializer):
	user = serializers.PrimaryKeyRelatedField()
	buses = BusSerializer(many=True)
	# buses = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="bus-detail")
	class Meta:
		model = Company
		fields = ('id', 'user', 'name', 'manager_phone', 'buses')
		owner = serializers.Field(source='owner.username')


#transaction Serializer
class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		fields = ('id','customer','schedule','cost','seat','transaction_time')
		owner = serializers.Field(source = 'owner.customer')

#schedule serializer
class ScheduleSerializer(serializers.ModelSerializer):

	capacity = serializers.Field()
	bus = BusSerializer()
	class Meta:
		model = Schedule
		fields = ('id','bus','datetime','capacity')

#serialize customers
class CustomerSerializer(serializers.ModelSerializer):
	user = serializers.PrimaryKeyRelatedField()
	class Meta:
		model = Customer
		fields = ('user','fname','lname','phone_number', 'account_number','address','gender','dob')
		owner = serializers.Field(source='owner.username')

