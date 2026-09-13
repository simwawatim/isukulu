from core.Utils.Decorators.TenantMember import tenant_member_required
from core.Forms.Departments.DepartmentsForms import DepartmentForm
from django.shortcuts import get_object_or_404, redirect, render
from core.models import Department, Teacher
from django.contrib import messages


@tenant_member_required
def Departments(request):
    departments = Department.objects.all().prefetch_related("subjects", "teachers")

    largest_department = max(departments, key=lambda d: d.teacher_count, default=None)

    context = {
        "departments": departments,
        "total_departments": departments.count(),
        "total_teaching_staff": Teacher.objects.filter(is_active=True).count(),
        "largest_department": largest_department.name if largest_department else "—",
        "vacant_hod_count": departments.filter(head_of_department__isnull=True).count(),
        "add_form": DepartmentForm(),
    }
    return render(request, "Tenant/Departments/Departments.html", context)


@tenant_member_required
def DepartmentCreate(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Department added.")
        else:
            messages.error(request, "Couldn't add that department — check the form and try again.")
    return redirect("departments")


@tenant_member_required
def DepartmentUpdate(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.success(request, "Department updated.")
        else:
            messages.error(request, "Couldn't save those changes — check the form and try again.")
    return redirect("departments")