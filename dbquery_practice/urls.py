from django.urls import path
from .views import student_create, student_list, standard_create, standard_list

urlpatterns = [
    path("", student_list, name="student_list"),
    path("create/", student_create, name="student_create"),
    path("standard_list/", standard_list, name="standard_list"),
    path("standard/", standard_create, name="standard_create"),
]
