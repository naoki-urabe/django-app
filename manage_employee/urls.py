from django.urls import path

from . import views

app_name = 'manage_employee'

urlpatterns = [
    path('show_employees', views.show_employees, name='show_employees')
]