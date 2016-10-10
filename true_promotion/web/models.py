from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=400)
	measure = models.CharField(max_length=50)
	creation_date = models.DateTimeField('creation date')
	update_date = models.DateTimeField('update date')
	price = models.FloatField(default=0) 

	def __str__(self):
		return self.name + " - " + self.description

