from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('student', 'meal', 'date', 'status')
    search_fields = ('student__email', 'meal__name')
    list_filter = ('date', 'status')
    ordering = ('-date',)