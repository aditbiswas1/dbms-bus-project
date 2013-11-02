from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from busapp import views

#patterns related to busstops
urlpatterns  = patterns('busapp.views',
	url(r'^busstops/$', views.BusStopList.as_view()),
	url(r'^busstops/(?P<pk>[0-9]+)/$', views.BusStopDetail.as_view()),
	)

#patterns related to universal routes
urlpatterns += patterns('busapp.views',
	url(r'^universal/$', views.UniversalRouteList.as_view()),
	url(r'^universal/(?P<pk>[0-9]+)/$', views.UniversalRouteDetail.as_view()),
	)

urlpatterns = format_suffix_patterns(urlpatterns)
