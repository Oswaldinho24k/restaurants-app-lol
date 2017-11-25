from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Restaurant
from .forms import RestaurantForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
#api
from rest_framework import viewsets
from .serializers import RestaurantSerializer


# Create your views here.
class RestaurantListView(View):
	def get(self, request, *args, **kwargs):
		q = request.GET.get('q')
		print(q)
		queryset = Restaurant.objects.all()
		if q:
			queryset = Restaurant.objects.all().filter(
				Q(name__icontains=q)|
				Q(owner__username__icontains=q)|
				Q(platillos__name__icontains=q)
				).distinct()
		template_name='restaurants/restaurant_list.html'
		context={
			'restaurants':queryset
		}
		return render(request, template_name, context)

class RestaurantDetailView(View):
	def get(self, request, pk):
		queryset = Restaurant.objects.get(pk=pk)
		template_name = 'restaurants/restaurant_detail.html'
		context={
			'rest':queryset
		}
		return render(request, template_name, context)




class RestaurantCreateView(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name='restaurants/restaurant_new.html'
		form = RestaurantForm
		context={
			'form':form
		}
		return render(request, template_name, context)
	def post(self, request):

		form = RestaurantForm(request.POST)

		if form.is_valid:
			new_restaurant = form.save(commit=False)
			new_restaurant.owner = request.user
			new_restaurant.save()

			return redirect('restaurants:list')

class RestaurantEditView(View):
	def get(self, request, pk):
		template_name='restaurants/restaurant_new.html'
		queryset = Restaurant.objects.get(pk=pk)
		form = RestaurantForm(instance=queryset)
		context = {
			'form':form
		}
		return render(request, template_name, context)

	def post(self, request, pk):
		queryset = Restaurant.objects.get(pk=pk)
		form = RestaurantForm(request.POST, instance=queryset)
		if form.is_valid:
			form.save()

		return redirect('restaurants:detail', pk)


class RestaurantDeleteView(View):
	def get(self, request, pk):
		queryset = Restaurant.objects.get(pk=pk)
		queryset.delete()

		return redirect('restaurants:list')


#for API
class RestaurantViewSet(viewsets.ModelViewSet):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantSerializer










