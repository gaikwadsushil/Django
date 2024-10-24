from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    transaction_type = models.CharField(max_length=20, choices=[('debit', 'Debit'), ('credit', 'Credit')])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount}  {self.transaction_type} "

class FraudAlert(models.Model):
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    alert_message = models.CharField(max_length=255)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Fraud Alert for Transaction {self.transaction.id}"
    