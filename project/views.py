from django.shortcuts import render
from .models import Student
def add_list(request):
    Student.objects.create(
        name='ridha',
        age=17,
        course='bca'
    )
def read_list(request):
    students=Student.objects.all()
    return render(request,'student.html',{'students':students})