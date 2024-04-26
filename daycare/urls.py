# urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('employee/add/', add_employee, name='add_employee'),
    path('employees/', employee_list, name='employee_list'),
    # Add other URL patterns as needed
]
