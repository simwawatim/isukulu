from django.shortcuts import render, redirect

def Dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "Tenant/Dashboard/Dashboard.html")


def Teachers(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "Tenant/Teachers/Teachers.html")

def Students(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "Tenant/Students/Students.html")

def Classes(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "Tenant/Classes/Classes.html")


def Subjects(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "Tenant/Subjects/Subjects.html")


def Exams(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "Tenant/Exams/Exams.html")


def Calandar(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "Tenant/Calendar/Calendar.html")


def Configuration(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "Tenant/Configuration/Configuration.html")