import datetime

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.db import connection
from django.shortcuts import render, redirect
from django.utils.text import slugify
from django_tenants.utils import schema_context

from customers.forms.company.company_forms import CompanyRegistrationForm
from customers.models import Client, Domain

RESERVED_SUBDOMAINS = {"public", "www", "admin"}


def home(request):
    return render(request, "Customers/Home.html")


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "Tenant/Dashboard/Dashboard.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            if connection.schema_name == "public":
                return redirect("admin_dashboard")
            return redirect("dashboard")
        messages.error(request, "Invalid email or password.")
    return render(request, "Customers/Login.html")

def logout_view(request):
    auth_logout(request)
    return redirect("login")


def admin_dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login")
 
    tenants = []
    for client in Client.objects.exclude(schema_name="public").order_by("name"):
        primary_domain = Domain.objects.filter(tenant=client, is_primary=True).first()
        tenants.append({
            "name": client.name,
            "domain": primary_domain.domain if primary_domain else None,
            "on_trial": client.on_trial,
            "paid_until": client.paid_until,
        })
 
    context = {
        "tenants": tenants,
        "total_schools": len(tenants),
        "trial_count": sum(1 for t in tenants if t["on_trial"]),
        "tenant_port": settings.TENANT_PORT,
        "page_title": "Schools",
    }
    return render(request, "Admin/Dashboard.html", context)


def generate_unique_subdomain(company_name):
    """Turn a school's name into a schema-safe, unused subdomain slug."""
    base_slug = slugify(company_name)[:63] or "school"

    slug = base_slug
    suffix = 1
    while slug in RESERVED_SUBDOMAINS or Client.objects.filter(schema_name=slug).exists():
        suffix += 1
        tail = f"-{suffix}"
        slug = f"{base_slug[:63 - len(tail)]}{tail}"

    return slug


def register_company(request):
    if request.method == "POST":
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            subdomain = generate_unique_subdomain(data["company_name"])

            tenant = Client(
                schema_name=subdomain,
                name=data["company_name"],
                paid_until=datetime.date.today() + datetime.timedelta(days=30),
                on_trial=True,
            )
            tenant.save()

            domain_name = f"{subdomain}.{settings.BASE_DOMAIN}"
            Domain.objects.create(
                domain=domain_name,
                tenant=tenant,
                is_primary=True,
            )

            with schema_context(tenant.schema_name):
                User.objects.create_user(
                    username=data["admin_email"],
                    email=data["admin_email"],
                    password=data["admin_password"],
                    first_name=data["admin_first_name"],
                    last_name=data["admin_last_name"],
                )

            port_suffix = f":{settings.TENANT_PORT}" if settings.TENANT_PORT else ""
            messages.success(
                request,
                f"Company registered. Sign in at "
                f"http://{domain_name}{port_suffix}/login/",
            )
            return redirect("home")
    else:
        form = CompanyRegistrationForm()

    return render(request, "Customers/RegisterCompany.html", {"form": form})