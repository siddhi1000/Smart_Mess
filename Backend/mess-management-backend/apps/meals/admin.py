from django.contrib import admin
from .models import Meal

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'available', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('available',)
    ordering = ('created_at',)