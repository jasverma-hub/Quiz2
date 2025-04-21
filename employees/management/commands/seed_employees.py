from django.core.management.base import BaseCommand
from employees.models import Employee
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with employee data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(5):  # 5 fake employees
            Employee.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number()[:20],
                department=random.choice(['HR', 'Engineering', 'Sales', 'Marketing']),
                designation=random.choice(['Manager', 'Executive', 'Intern', 'Team Lead']),
                salary=round(random.uniform(30000, 120000), 2),
                date_of_joining=fake.date_between(start_date='-5y', end_date='today')
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded employee data'))
