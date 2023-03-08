from django.db import models
import datetime
class Users(models.Model):
    name = models.CharField(max_length=100)
    emailId = models.EmailField(max_length=100)
    phoneNumber = models.BigIntegerField(blank=True)
    age = models.PositiveIntegerField(blank=True)
    GENDER_CHOICES = [(0, 'Male'), (1, 'Female')]
    gender = models.IntegerField(choices=GENDER_CHOICES)
    departuredate = models.DateField(default=datetime.date.today)
    departuretime = models.TimeField(default=datetime.time(00, 00))
    returndate = models.DateField(default=datetime.date.today)
    returntime = models.TimeField(default=datetime.time(00, 00))
    travelDestination = models.CharField(max_length=100)
    package = models.CharField(max_length=100)

class FoodService(models.Model):
    food = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images/',null=True)

class FlightService(models.Model):
    flight = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images/',null=True)

class TravelService(models.Model):
    travel = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images/',null=True)

class HotelService(models.Model):
    hotel = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images/',null=True)

class Location(models.Model):
    country = models.CharField(max_length=100)
    cityName = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='static/images/',null=True)

class Services(models.Model):
    serviceName = models.CharField(max_length=100)
    description = models.CharField(max_length=500,null=True)
    image = models.ImageField(upload_to='static/images/',null=True)

