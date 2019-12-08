from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager
# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
        email = models.EmailField(
                verbose_name='Email Field',
                max_length=255,
                unique=True
                )
        name=models.CharField(max_length=30)
        active = models.BooleanField(default=True)
        staff = models.BooleanField(default=False)
        admin = models.BooleanField(default=False)
        USERNAME_FIELD='email'
        REQUIRED_FIELDS=['name']

        def __str__(self):
                return self.email

        @property
        def is_admin(self):
                return self.admin
        
        @property
        def is_active(self):
                return self.active

        @property
        def is_staff(self):
                return self.staff
        

        objects=UserManager()

class Airport(models.Model):
	Airport_id= models.CharField(max_length=10, unique=True)
	Airport_name = models.CharField(max_length=30)


class Flights(models.Model):
	Flight_no = models.IntegerField()
	source = models.OneToOneField( Airport, on_delete=models.CASCADE, related_name='source')
	destination = models.OneToOneField( Airport, on_delete=models.CASCADE, related_name='destination')
	departure_time =models.DateTimeField()
	arrival_time = models.DateTimeField()

class Bookings(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	flight = models.OneToOneField(Flights, on_delete=models.CASCADE)
	number_of_passengers = models.IntegerField()
	total_price = models.IntegerField()

