from django.contrib import admin
from .models import Menu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'available_from', 'available_until')
    search_fields = ('name', 'description')
    list_filter = ('available_from', 'available_until')
    ordering = ('available_from',)