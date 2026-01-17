from django.urls import path
from .views import BillingListView, BillingDetailView

urlpatterns = [
    path('', BillingListView.as_view(), name='billing-list'),
    path('<int:pk>/', BillingDetailView.as_view(), name='billing-detail'),
]