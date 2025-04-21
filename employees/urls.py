from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeListCreateAPIView.as_view(), name='employee-list-create'),  # List or create employee
    path('<int:pk>/', views.EmployeeDetailAPIView.as_view(), name='employee-detail'),    # Detail view

    path('employee_chart/', views.employee_chart, name='employee_chart'),                # Chart HTML page
    path('chart/data/', views.EmployeeChartDataAPIView.as_view(), name='employee_chart_data'),  # Chart Data API
]
