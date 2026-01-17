from django.contrib import admin
from .models import Billing

@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'amount_due', 'payment_status', 'created_at')
    search_fields = ('student__email', 'payment_status')
    list_filter = ('payment_status', 'created_at')
    ordering = ('-created_at',)