from django.conf.urls import url, include
from django.contrib import admin
from restaurants import urls as restaurantUrls
from accounts import urls as accUrls
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from platillos import urls as platilloUrls
#api
from rest_framework import routers
from restaurants.views import RestaurantViewSet

class HomeView(TemplateView):
	template_name='home.html'


router = routers.DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^restaurants/', include(restaurantUrls, namespace='restaurants')),
    url(r'^accounts/', include(accUrls, namespace='accounts')),
    url(r'^login/', auth_views.login,  name='login'),
    url(r'^logout/', auth_views.logout, name='logout'),
    url(r'^platillos/', include(platilloUrls, namespace="platillos")),
    #api
    url(r'^api/', include(router.urls)),

]
