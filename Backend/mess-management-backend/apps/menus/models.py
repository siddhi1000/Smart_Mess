from django.db import models

class Menu(models.Model):
    meal_type = models.CharField(max_length=50)  # e.g., Breakfast, Lunch, Dinner
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available_days = models.CharField(max_length=100)  # e.g., "Monday, Tuesday, Wednesday"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.meal_type} - {self.description}"