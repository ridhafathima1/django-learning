from django.shortcuts import render
from .models import Student
def add_students(request):
    Student.objects.create(
        name='ridha',
        age=17,
        course='bca'
    )
def read_students(request):
    student=Student.objects.all()

    return render(request,'student.html',{'students':student})