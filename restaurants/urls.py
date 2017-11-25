from django.conf.urls import url
from .views import RestaurantListView, RestaurantDetailView, RestaurantCreateView, RestaurantEditView, RestaurantDeleteView


urlpatterns=[
	url(r'^$', RestaurantListView.as_view(), name='list'),
	url(r'^(?P<pk>[0-9]+)/$', RestaurantDetailView.as_view(), name='detail'),
	url(r'^edit/(?P<pk>[0-9]+)/$', RestaurantEditView.as_view(), name='edit'),
	url(r'^delete/(?P<pk>[0-9]+)/$', RestaurantDeleteView.as_view(), name='delete'),
	url(r'^new/$', RestaurantCreateView.as_view(), name='new')
]