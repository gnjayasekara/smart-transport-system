from django.db import models
from users.models import User

class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ('topup', 'Top-up'),
        ('fare', 'Fare Payment'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.transaction_type} - ${self.amount}"
