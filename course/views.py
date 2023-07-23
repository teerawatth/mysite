from django.shortcuts import render
from .models import *

def index(request):
    course = Course.objects.all()
    return render(request,'course/index.html',{'course': course,})

def coure_detail(request, pk):
    course = Course.objects.get(id=pk)
    return render(request,'course/coursedetail.html',{'c': course})

def classwork(request):
    return render(request,'course/classwork.html')

def people(request):
    std = Student.objects.all()
    lcr = Lecturer.objects.all()
    return render(request,'course/people.html',{"std":std, "lcr":lcr})

def grades(request):
    return render(request,'course/grades.html')

def lecturer(request):
    lecturers = Lecturer.objects.all()
    return render(request,'course/lecturer.html',{'lecturer': lecturers,})

def lecturer_profile(request, pk):
    lecturers = Lecturer.objects.get(id=pk)
    return render(request,'course/lecturerprofile.html',{'lecturer': lecturers})

def student(request):
    students = Student.objects.all()
    return render(request,'course/student.html',{'student': students,})

def student_profile(request, pk):
    students = Student.objects.get(id=pk)
    return render(request,'course/studentprofile.html',{'student': students})