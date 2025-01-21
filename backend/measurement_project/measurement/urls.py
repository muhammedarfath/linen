from django.urls import path
from .views import *

urlpatterns = [
path('mens/',MensMeasurement.as_view()),
path('women/', WomenMeasurement.as_view()),
path('order-details/', OrderDetailsView.as_view()),
path('order-count/', OrderCountView.as_view()),
path('update-status/<int:order_id>/', UpdateOrderStatusView.as_view()),
path('edit/<int:order_id>/',OrderDetailUpdateView.as_view()),


]
