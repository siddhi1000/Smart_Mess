from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('student', 'rating', 'created_at')
    search_fields = ('student__email', 'comments')
    list_filter = ('rating', 'created_at')
    ordering = ('-created_at',)