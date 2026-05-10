from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home'),

    path('employees/register/', views.register, name='register'),

    path('employees/login/', views.login, name='login'),

    path('employees/logout/', views.logout_view, name='logout'),

    path('employees/dashboard/', views.dashboard, name='dashboard'),

    path('employees/employee-list/', views.employee_list, name='employees_list'),
    path('admin-dashboard/',views.admin_dashboard,name='admin_dashboard'),

    path(
        'approve/<int:id>/',
        views.approve_employee,
        name='approve_employee'
    ),

    path(
        'reject/<int:id>/',
        views.reject_employee,   
    ),
    path('company-policies/', views.policies, name='policies'),
    path('hr-instructions/', views.hr_instructions, name='hr_instructions'),
    path('upload-documents/', views.upload_documents, name='upload_documents'),
    path('joining-process/', views.joining_process, name='joining_process'),
    path('dashboard-access/', views.dashboard_access, name='dashboard_access'),
    path('approval-status/', views.approval_status, name='approval_status'),
    path('company-details/', views.company_details, name='company_details'),
    path('employees/add/', views.add_employee, name='add_employee'),
      
]