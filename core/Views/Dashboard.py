from django.shortcuts import render, redirect

def Dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "Tenant/Dashboard/Dashboard.html")