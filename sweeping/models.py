from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MaxValueValidator

direction_choices = (('N','North'),('S','South'),('E', 'East'),('W','West'))
day_choices = ((1,'1st'),(2,'2nd'),(3,'3rd'),(4,'4th'))



class Weekday(models.Model):
	num = models.IntegerField()
	title = models.CharField(max_length=100)
	def __str__(self):
		return str(self.title)
	def sweeps(self):
		return Sweep.objects.filter(day=self.title)
dir_choices = (("NS","North - South"),("EW","East - West"))

class Street (models.Model):
	name= models.CharField(max_length=200)
	direction = models.CharField(max_length=10, choices = dir_choices)


	def __str__(self):
		return str(self.name)

class Sweep(models.Model):
	rte = models.PositiveSmallIntegerField(default=0)
	street_name = models.CharField(max_length = 200)
	from_address = models.IntegerField()
	to_address = models.IntegerField()
	day = models.ForeignKey('Weekday',blank=True, null=True,)
	of_month = models.IntegerField()
	time = models.CharField(max_length=3)
	side = models.CharField(max_length = 10)
	from_street = models.CharField(max_length = 200)
	to_street = models.CharField(max_length=200)
	optout = models.IntegerField(blank=True, null=True,)

	def __str__(self):
		return str(self.street_name)

