from django.db import models

class Employee(models.Model):
    FULL_TIME = 'full_time'
    HALF_TIME = 'half_time'
    
    WORK_CHOICES = [
        (FULL_TIME, 'Full Time'),
        (HALF_TIME, 'Half Time'),
    ]

    name = models.CharField(max_length=100)
    work_type = models.CharField(max_length=20, choices=WORK_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Add the salary field
    
    def calculate_salary(self):
        if self.work_type == self.FULL_TIME:
            return 10000
        elif self.work_type == self.HALF_TIME:
            return 5000
        else:
            return 0  # Default or handle other cases here
    
    def save(self, *args, **kwargs):
        self.salary = self.calculate_salary()  # Calculate salary before saving
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
