from django.shortcuts import render
from django.views import View
from manage_employee.models.employee import Employee
from manage_employee.forms.employee_form import EmployeeForm
from django.contrib.auth.mixins import LoginRequiredMixin

class manageEmployeeView(LoginRequiredMixin, View):
    #認証してない場合のリダイレクト先
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        form = EmployeeForm()
        context = {
            'form': form,
            'employees': employees
        }
        return render(request, 'show_employees.html', context)
    def post(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        #入力データを取得
        form = EmployeeForm(request.POST)
        #データの検証
        is_valid = form.is_valid()
        #登録
        if "register" in request.POST:
            form.save()
        #更新
        if "update" in request.POST:
            employee = Employee.objects.get(id=int(request.POST["update_id"]))
            employee.age = form.cleaned_data.get("age")
            employee.save()
            employees = Employee.objects.all()
        #検索
        if "select" in request.POST:
            employees = Employee.objects.filter(age=form.cleaned_data.get("age"))
        #削除
        if "delete" in request.POST:
            user = Employee.objects.get(id=int(request.POST["delete_id"]))
            user.delete()
        context = {
            'form': form,
            'employees': employees
        }
        return render(request, 'show_employees.html', context)