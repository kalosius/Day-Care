

from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Redirect to employee list page after successful form submission
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})


# views.py




def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})
