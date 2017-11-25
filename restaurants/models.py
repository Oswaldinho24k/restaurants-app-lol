from django.db import models
from django.core.urlresolvers import reverse
#from django.contrib.gis.db.models import GeoManager
from location_field.models.plain import PlainLocationField
from django.contrib.auth.models import User

# Create your models here.

class Restaurant(models.Model):
	name = models.CharField(max_length=140)
	#location = PlainLocationField(based_fields=['city'], zoom=7)
	owner = models.ForeignKey(User, related_name='restaurants')
	is_open = models.TimeField(db_index=True)
	is_closed = models.TimeField(db_index=True)

	class Meta:
		ordering=['-is_open']
	

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('restaurants:detail', kwargs={'pk':self.pk})

