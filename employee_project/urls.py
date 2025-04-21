from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from employees.views import health_check
from employees.views import EmployeeExportCSVAPIView, EmployeeExportExcelAPIView, EmployeeChartDataAPIView

# Swagger Schema config
schema_view = get_schema_view(
    openapi.Info(
        title="Employee API",
        default_version='v1',
        description="API documentation for the Employee Management System",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[],  # <-- Yahan empty (Swagger khud me handle karega)
)

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),
    
    # Redirect root URL to the employees API
    path('', lambda request: HttpResponseRedirect('api/employees/')),
    
    # Include employee-related API URLs
    path('api/employees/', include('employees.urls')),  # This includes the employees app's URLs
    
    # JWT authentication token URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtain JWT token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh JWT token
    
    # Swagger UI endpoint for API documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

     # Health check endpoint
    path('health/', health_check, name='health_check'),  # Health check endpoint

     # URL for exporting employee data to CSV
    path('api/employees/export/csv/', EmployeeExportCSVAPIView.as_view(), name='export_employees_csv'),
    
    # URL for exporting employee data to Excel
    path('api/employees/export/excel/', EmployeeExportExcelAPIView.as_view(), name='export_employees_excel'),

    path('api/employees/chart/data/', EmployeeChartDataAPIView.as_view(), name='employee_chart_data'),
]
