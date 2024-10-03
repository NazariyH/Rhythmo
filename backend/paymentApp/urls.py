from django.urls import path
from . import views

urlpatterns = [
    path('payment-process/', views.PaymentProcess.as_view(), name='payment-process'),
]