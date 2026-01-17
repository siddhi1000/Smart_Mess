from django.test import TestCase
from apps.bookings.models import Booking
from django.contrib.auth import get_user_model

User = get_user_model()

class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@college.edu',
            password='testpassword'
        )
        self.booking = Booking.objects.create(
            user=self.user,
            meal_type='Lunch',
            date='2024-04-01',
            status='Booked'
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.user, self.user)
        self.assertEqual(self.booking.meal_type, 'Lunch')
        self.assertEqual(self.booking.status, 'Booked')

    def test_booking_str(self):
        self.assertEqual(str(self.booking), f"{self.booking.meal_type} - {self.booking.date}")

    def test_booking_status_update(self):
        self.booking.status = 'Cancelled'
        self.booking.save()
        self.assertEqual(self.booking.status, 'Cancelled')