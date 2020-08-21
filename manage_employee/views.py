from django.shortcuts import render
from django.views import View
from .models import Employee

class manageEmployeeView(View):
    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        context = {
            'employees': employees
        }
        return render(request, 'show_employees.html', context)
show_employees = manageEmployeeView.as_view()