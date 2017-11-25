from django.conf.urls import url
from .views import PlatilloListView, PlatilloDetailView, PlatilloCreateView, PlatilloUpdateView, PlatilloDeleteView


urlpatterns = [
	url(r'^$', PlatilloListView.as_view(), name="list"),
	url(r'^(?P<pk>[0-9]+)/$', PlatilloDetailView.as_view(), name="detail"),
	url(r'^new/$', PlatilloCreateView.as_view(), name="new"),
	url(r'^update/(?P<pk>[0-9])/$', PlatilloUpdateView.as_view(), name="update"),
	url(r'^delete/(?P<pk>[0-9])/$', PlatilloDeleteView.as_view(), name="delete"),
]