from django.urls import path
from .views import (
    admin_login,
    login_signup,
    verify_otp,
    verify_login_otp,
    dashboard,
    logout_view,
    police_view,
    pviewcase_view,
    overview,
    pcasecompleted,
    emergency,
    user_dashboard_view,
    userviewcase,
    verify_admin_login_otp,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('admin/login/', admin_login, name='admin_login'),  # Custom admin login
    path('login-signup/', login_signup, name='login_signup'),
    path('verify_otp/', verify_otp, name='verify_otp'),
    path('verify_login_otp/', verify_login_otp, name='verify_login_otp'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('police/', police_view, name='police'),
    path('pviewcase/', pviewcase_view, name='pviewcase'),
    path('overview/', overview, name='overview'),
    path('pcasecompleted/', pcasecompleted, name='pcasecompleted'),
    path('emergency/', emergency, name='emergency'),
    path('user-dashboard/', user_dashboard_view, name='UserDashboard'),
    path('userviewcase',userviewcase, name='userviewcase'),
    path('admin/verify-otp/', verify_admin_login_otp, name='verify_admin_login_otp'),
]
