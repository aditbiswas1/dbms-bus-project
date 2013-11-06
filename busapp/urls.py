from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from busapp import views

#patterns related to busstops
urlpatterns  = patterns('busapp.views',
	url(r'^busstops/$', views.BusStopList.as_view(),name='busstop-list'),
	url(r'^busstops/(?P<pk>[0-9]+)/$', views.BusStopDetail.as_view(), name='busstop-detail'),
	)

#patterns related to universal routes
urlpatterns += patterns('busapp.views',
	url(r'^universal/$', views.UniversalRouteList.as_view(), name='universal-route-list'),
	url(r'^universal/(?P<pk>[0-9]+)/$', views.UniversalRouteDetail.as_view(), name='universal-route-detail'),
	)

#patterns related to routestops
urlpatterns += patterns('busapp.views',
	url(r'^routestops/$', views.RouteStopList.as_view(),name='routestop-list'),
	url(r'^routestops/(?P<pk>[0-9]+)/$', views.RouteStopDetail.as_view(), name='routestop-detail'),
	)


#patterns related to users
urlpatterns += patterns('busapp.views',
	url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
	)

#patterns related to companies
urlpatterns += patterns('busapp.views',
	url(r'^companies/$', views.CompanyList.as_view(), name='company-list'),
	url(r'^companies/(?P<pk>[0-9]+)/$', views.CompanyDetail.as_view(), name='company-detail'),
	)

#patterns related to bus
urlpatterns += patterns('busapp.views',
	url(r'^buses/$', views.BusList.as_view(), name='bus-list'),
	url(r'^buses/(?P<pk>[0-9]+)/$', views.BusDetail.as_view(), name='bus-detail'),
	)

#format the suffix of the patterns to accept data types of html, json , xml
urlpatterns = format_suffix_patterns(urlpatterns)