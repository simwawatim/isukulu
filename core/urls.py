from core.Views.AdminViews.Views import Calandar, Classes, Configuration, Dashboard, Exams, Students, Subjects, Teachers
from django.urls import path

urlpatterns = [
    path("dashboard/", Dashboard, name="dashboard"),
    path("teachers/", Teachers, name="teachers"),
    path("students/", Students, name="students"),
    path("classes/", Classes, name="classes"),
    path("subjects/", Subjects, name="subjects"),
    path("exams/", Exams, name="exams"),
    path("calendar/", Calandar, name="calendar"),
    path("configuration/", Configuration, name="configuration"),
]