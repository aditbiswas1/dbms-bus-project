from rest_framework import serializers
from busapp.models import BusStop, UniversalRoute
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
	source = serializers.RelatedField()
	destination = serializers.RelatedField()
	class Meta:
		model = UniversalRoute
		fields = ('id', 'source', 'destination')