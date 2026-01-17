from django.urls import path
from .views import BookingListView, BookingDetailView, CreateBookingView

urlpatterns = [
    path('bookings/', BookingListView.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
    path('bookings/create/', CreateBookingView.as_view(), name='create-booking'),
]