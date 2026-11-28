from django.urls import path 
from . import views
urlpatterns=[
    path('students/',views.add_students,name='student_list')
]