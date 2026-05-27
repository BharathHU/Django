import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fakeproject.settings')
django.setup()
from myapp.models import Employee
from faker import Faker
f=Faker('en-IN')
def populate(n):
    for i in range(n):
        fname=f.name()
        femail=f.email()
        fplace=f.address()
        fposition=f.job()
        fdepartment=f.random_element(elements=('HR', 'Finance', 'Engineering', 'Sales', 'Marketing', 'Legal', 'Admin'))
        fsalary=f.random_int(min=30000,max=150000)
        Employee.objects.create(
            name=fname,
            email=femail,
            department=fdepartment,
            place=fplace,
            position=fposition,
            salary=fsalary,
        )

if __name__ == '__main__':
    populate(20)

