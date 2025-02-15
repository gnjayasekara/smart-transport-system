import uuid
from django.db import models
from users.models import User

class ParkingTicket(models.Model):
    ticket_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_number = models.CharField(max_length=15)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Ticket {self.ticket_id} - {self.vehicle_number}"
