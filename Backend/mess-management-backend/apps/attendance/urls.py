from django.urls import path
from .views import AttendanceListView, AttendanceDetailView, MarkAttendanceView

urlpatterns = [
    path('', AttendanceListView.as_view(), name='attendance-list'),
    path('<int:pk>/', AttendanceDetailView.as_view(), name='attendance-detail'),
    path('mark/', MarkAttendanceView.as_view(), name='mark-attendance'),
]