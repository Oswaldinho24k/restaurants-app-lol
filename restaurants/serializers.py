from rest_framework import serializers
from .models import Restaurant
from django.contrib.auth.models import User
from platillos.models import Platillo


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'id']

class PlatilloSerializer(serializers.ModelSerializer):
	class Meta:
		model = Platillo
		fields = ['name']

class RestaurantSerializer(serializers.ModelSerializer):
	owner = UserSerializer(many=False, read_only=True)
	platillos = PlatilloSerializer(many=True, read_only=True)
	class Meta:
		model = Restaurant
		fields = '__all__'
