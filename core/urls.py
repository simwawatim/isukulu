from core.Views.AdminViews.Departments.DepartmentsView import DepartmentCreate, DepartmentUpdate, Departments
from core.Views.AdminViews.Views import Attendance, Calandar, Classes, Configuration, Dashboard, Exams, Results, Students, Subjects, Teachers, Timetable
from django.urls import path

urlpatterns = [
    path("dashboard/", Dashboard, name="dashboard"),
    path("teachers/", Teachers, name="teachers"),
    path("students/", Students, name="students"),
    path("classes/", Classes, name="classes"),
    path("subjects/", Subjects, name="subjects"),
    path("exams/", Exams, name="exams"),
    path("calendar/", Calandar, name="calendar"),
    path("departments/", Departments, name="departments"),
    path("departments/add/", DepartmentCreate, name="department_create"),
    path("departments/<int:pk>/edit/", DepartmentUpdate, name="department_update"),
    path("configuration/", Configuration, name="configuration"),
    path("attendance/", Attendance, name="attendance"),
    path("results/", Results, name="results"),
    path("timetable/", Timetable, name="timetable"),
    
]