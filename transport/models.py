from django.db import models
from users.models import User
from parking.models import ParkingTicket

class TransportVehicle(models.Model):
    vehicle_id = models.CharField(max_length=20, unique=True)
    driver = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True)
    vehicle_type = models.CharField(max_length=20, choices=[('bus', 'Bus'), ('train', 'Train')])
    route_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.vehicle_type.capitalize()} - {self.vehicle_id}"

class LiveLocation(models.Model):
    vehicle = models.OneToOneField(TransportVehicle, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vehicle} - Last Update: {self.last_updated}"

class TransportPass(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parking_ticket = models.OneToOneField(ParkingTicket, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    expiration_date = models.DateTimeField()

    def __str__(self):
        return f"Pass for {self.user.username} - Active: {self.is_active}"
