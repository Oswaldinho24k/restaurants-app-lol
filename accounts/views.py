from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserRegistrationForm

# Create your views here.

class ProfileView(View):
	def get(self, request):
		template_name='accounts/profile.html'

		context = {

		}

		return render(request, template_name,context)

class RegistrationView(View):
	def get(self, request):
		template_name = 'accounts/registration.html'
		form = UserRegistrationForm
		context = {
			'form':form
		}
		return render(request, template_name, context)

	def post(self, request):

		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data['password'])
			new_user.save()
		return redirect('login')




