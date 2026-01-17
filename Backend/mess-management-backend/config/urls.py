from django.urls import path, include

urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('menus/', include('apps.menus.urls')),
    path('meals/', include('apps.meals.urls')),
    path('bookings/', include('apps.bookings.urls')),
    path('attendance/', include('apps.attendance.urls')),
    path('billing/', include('apps.billing.urls')),
    path('feedback/', include('apps.feedback.urls')),
]