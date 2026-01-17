from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'meal', 'date', 'status')
    search_fields = ('student__name', 'meal__name')
    list_filter = ('date', 'status')