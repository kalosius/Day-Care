from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    salary = forms.DecimalField(label='Salary', disabled=False)

    class Meta:
        model = Employee
        fields = ['name', 'work_type', 'salary']
        labels = {
            'name': 'Name',
            'work_type': 'Work Type',
        }
