from django.urls import path
from customers.Views import CompanyViews as views
from customers.Views.Schools import SchoolsView as schools_views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("schools/", schools_views.schools, name="schools"),
    path("tiers/", schools_views.tiers, name="tiers"),
    path("tiers/add/", schools_views.add_tier, name="add_tier"),
    path("tiers/<int:tier_id>/edit/", schools_views.edit_tier, name="edit_tier"),
    path("tiers/<int:tier_id>/delete/", schools_views.delete_tier, name="delete_tier"),
    path("register/", views.register_company, name="register_company"),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]