from django.urls import path
from customers.Views import CompanyViews as views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_company, name="register_company"),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]