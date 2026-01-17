from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey('meals.Meal', on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        unique_together = ('user', 'meal', 'booking_date')

    def __str__(self):
        return f"{self.user.username} - {self.meal.name} on {self.booking_date}"