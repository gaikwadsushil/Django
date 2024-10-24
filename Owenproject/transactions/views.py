from django.shortcuts import render
from .models import Transaction, FraudAlert

# Create your views here.
def detect_fraud():
    # Filter transactions with an amount greater than 50,000
    suspicious_transactions = Transaction.objects.filter(amount__gt=50000)  # Example threshold

    for transaction in suspicious_transactions:
        # Avoid duplicate alerts
        if not FraudAlert.objects.filter(transaction=transaction).exists():
            FraudAlert.objects.create(
                transaction=transaction,
                alert_message=f"High-value transaction detected: {transaction.amount}"  # Create a new alert for each suspicious transaction
            )

def transaction_list(request):
    detect_fraud()  # Call fraud detection logic
    transactions = Transaction.objects.all()  # Use the correct model reference
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})