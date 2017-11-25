from django.db import models
from django.core.urlresolvers import reverse
from restaurants.models import Restaurant

# Create your models here.

class Platillo(models.Model):

	name = models.CharField(max_length=140)
	restaurant = models.ForeignKey(Restaurant, related_name='platillos')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('platillos:detail', kwargs={'pk':self.pk})

