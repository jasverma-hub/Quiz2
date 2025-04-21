from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeListCreateAPIView.as_view(), name='employee-list-create'),  # List or create employee
    path('<int:pk>/', views.EmployeeDetailAPIView.as_view(), name='employee-detail'),  # Detail view
]
