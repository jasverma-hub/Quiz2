
# Employee Management System

This is an Employee Management System built using Django and Django Rest Framework (DRF). It allows users to manage employee data, visualize employee distribution by department, and export the employee data in CSV and Excel formats.

## Features

- **Employee Management**: CRUD operations for employee records.
- **Search & Filter**: Search employees by first name, last name, and department.
- **Export to CSV/Excel**: Export employee data in CSV and Excel formats.
- **Data Visualization**: Visualize employee distribution by department using charts.
- **API Documentation**: Swagger UI to interact with the API endpoints.
- **Rate Limiting**: Apply rate limiting for both authenticated and unauthenticated users.

## Technologies Used

- **Django**: Backend framework.
- **Django Rest Framework (DRF)**: API framework for building RESTful services.
- **Chart.js**: For rendering employee distribution charts.
- **Openpyxl**: To work with Excel files.
- **CSV**: To export data in CSV format.
- **Django Filter**: For advanced filtering and search functionality.
- **JWT Authentication**: To authenticate users.

## Installation & Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/jasverma-hub/Quiz2.git
   cd Quiz2
   ```

2. **Install dependencies**:

   Create and activate a virtual environment (if you haven't already):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

   Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**:

   Run migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (optional)**:

   If you need admin access, create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

5. **Run the server**:

   Start the development server:

   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://127.0.0.1:8000/`.

## API Endpoints

- **GET /api/employees/**: List all employees (with search and filter).
- **POST /api/employees/**: Create a new employee.
- **GET /api/employees/{id}/**: Retrieve details of a specific employee.
- **PUT /api/employees/{id}/**: Update a specific employee.
- **DELETE /api/employees/{id}/**: Delete a specific employee.
- **GET /api/employees/export/csv/**: Export employees in CSV format.
- **GET /api/employees/export/excel/**: Export employees in Excel format.
- **GET /api/employees/chart/data/**: Get employee distribution by department (for chart visualization).

## Data Visualization

The employee distribution by department is visualized using a **Bar Chart**. You can access this visualization at the following endpoint:

- **URL**: `/employees/employee-chart/`

This page will render a chart showing the number of employees in each department.

## Authentication

The API requires **JWT authentication**. You can obtain the token by sending a POST request to:

- **POST /api/token/**: Receive the access token using the credentials (username, password).
- **Authorization Header**: Bearer token must be included in the header for all authenticated requests.

Example:
```bash
Authorization: Bearer <your_token>
```

## Swagger UI

For interactive API documentation, Swagger UI is available at:

- **URL**: `/swagger/`

## Health Check

The API health status can be checked at:

- **URL**: `/health/`

