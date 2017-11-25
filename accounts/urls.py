from django.conf.urls import url
from .views import ProfileView, RegistrationView

urlpatterns=[
	url(r'^profile/$', ProfileView.as_view(), name='profile'),
	url(r'^register/$', RegistrationView.as_view(), name='register')
]