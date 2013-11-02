from busapp.serializers import BusStopSerializer, UniversalRouteSerializer

from rest_framework import generics

from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from busapp.models import BusStop, UniversalRoute


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
