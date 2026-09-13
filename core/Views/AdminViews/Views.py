from core.Utils.Decorators.TenantMember import tenant_member_required
from django.shortcuts import render



@tenant_member_required
def Dashboard(request):
    return render(request, "Tenant/Dashboard/Dashboard.html")


@tenant_member_required
def Teachers(request):
    return render(request, "Tenant/Teachers/Teachers.html")


@tenant_member_required
def Students(request):
    return render(request, "Tenant/Students/Students.html")


@tenant_member_required
def Classes(request):
    return render(request, "Tenant/Classes/Classes.html")


@tenant_member_required
def Subjects(request):
    return render(request, "Tenant/Subjects/Subjects.html")



@tenant_member_required
def Exams(request):
    return render(request, "Tenant/Exams/Exams.html")


@tenant_member_required
def Calandar(request):
    return render(request, "Tenant/Calendar/Calendar.html")


@tenant_member_required
def Configuration(request):
    return render(request, "Tenant/Configuration/Configuration.html")


@tenant_member_required
def Attendance(request):
    return render(request, "Tenant/Attendance/Attendance.html")


@tenant_member_required
def Results(request):
    return render(request, "Tenant/Results/Results.html")


@tenant_member_required
def Timetable(request):
    return render(request, "Tenant/Timetable/Timetable.html")