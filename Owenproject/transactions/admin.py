from django.contrib import admin
from .models import Transaction, FraudAlert

# Register your models here.
admin.site.register(Transaction)
admin.site.register(FraudAlert)