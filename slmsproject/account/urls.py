from django.urls import path
from .views import (
    home,
    register,
    login_view,
    profile,
    staff_dashboard,
    apply_leave,
    leave_status,
    admin_approve_leaves,
    staff_approve_leave,
    staff_reject_leave,
)

urlpatterns = [
    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),

    # Staff features
    path('staff/', staff_dashboard, name='staff_dashboard'),
    path('staff/apply/', apply_leave, name='staff_apply_leave'),
    path('staff/status/', leave_status, name='staff_leave_status'),

    # Admin approvals
    path('staff/admin/leaves/', admin_approve_leaves, name='admin_approve_leaves'),
    path('staff/admin/leaves/<int:leave_id>/approve/', staff_approve_leave, name='staff_approve_leave'),
    path('staff/admin/leaves/<int:leave_id>/reject/', staff_reject_leave, name='staff_reject_leave'),

    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
]




