from django.shortcuts import redirect, render
from django.contrib import messages
from placement.models import Placed_student
from student.models import *

# Create your views here.
def home(request):
    return render(request,'student/home.html')

def aboutus(request):
    return render(request,'student/aboutus.html')

def aws(request):
    return render(request,'student/aws.html')

def java(request):
    return render(request,'student/java.html')

def placement(request):
    students=Placed_student.objects.all()
    context={
        'students':students 
    }
    return render(request,'student/placement.html',context)

def registration(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        city=request.POST.get('city')
        degree=request.POST.get('degree')
        percentage=request.POST.get('percentage')
        course=request.POST.get('course')
        fee=request.POST.get('fee')
        s1=Student_details(name=name,email=email,city=city,degree=degree,percentage=percentage,course=course,fee=fee)
        s1.save()
        messages.info(request,"register sucessfully...")
        return redirect('home')

    return render(request,'student/registration.html')

def python(request):
    return render(request,'student/python.html')
