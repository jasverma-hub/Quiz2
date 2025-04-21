import csv
import openpyxl
from django.http import HttpResponse
from rest_framework import generics
from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from collections import Counter
from rest_framework.permissions import AllowAny

# Health check view (moved outside the class)
def health_check(request):
    return JsonResponse({"status": "OK"})

def employee_chart(request):
    return render(request, 'employees/employee_chart.html')  # Ensure the correct template path

class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access this view
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['first_name', 'last_name', 'department']  # Fields to search
    throttle_classes = [UserRateThrottle, AnonRateThrottle]  # Apply throttling here

    @method_decorator(cache_page(60 * 5))  # Cache GET requests for 5 minutes
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class EmployeeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]  # Ensure only authenticated users can access this view and only admins can modify or delete

# Export to CSV view
class EmployeeExportCSVAPIView(generics.ListAPIView):  # 👈 GenericAPIView -> ListAPIView
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['first_name', 'last_name', 'department']
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())  # 👈 Apply search & filters here!

        # Create a CSV response
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="employees.csv"'

        writer = csv.writer(response)
        writer.writerow(['ID', 'First Name', 'Last Name', 'Department', 'Position', 'Email'])

        for employee in queryset:
            writer.writerow([
                employee.id, employee.first_name, employee.last_name,
                employee.department, employee.position, employee.email
            ])

        return response

# Export to Excel view
class EmployeeExportExcelAPIView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        # Get all employee data
        employees = Employee.objects.all()

        # Create a new workbook and add a sheet
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.title = 'Employees'

        # Add header row
        sheet.append(['ID', 'First Name', 'Last Name', 'Department', 'Position', 'Email'])

        # Add employee data
        for employee in employees:
            sheet.append([employee.id, employee.first_name, employee.last_name, employee.department, employee.position, employee.email])

        # Create a response object to serve the Excel file
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="employees.xlsx"'

        wb.save(response)
        return response
    
class EmployeeChartDataAPIView(APIView):
    permission_classes = [AllowAny]  # <-- Add this line
    def get(self, request, *args, **kwargs):
        # Fetch all employee data
        employees = Employee.objects.all()

        # Group employees by department and count the number of employees in each department
        departments = [employee.department for employee in employees]
        department_count = dict(Counter(departments))

        # Return the data as a JSON response
        return Response(department_count)
