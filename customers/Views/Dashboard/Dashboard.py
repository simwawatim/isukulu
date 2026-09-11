from customers.models import Client, Domain
from django.shortcuts import render, redirect


def dashboard(request):
    return render(request, 'dashboard.html')