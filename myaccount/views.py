from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User

from student.models import Student_details
# Create your views here.
def signup(request):
    if request.method=='POST':
        fn=request.POST.get('fname')
        ln=request.POST.get('lname')
        un=request.POST.get('uname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if pass1==pass2:
            if User.objects.filter(username=un).exists():
                messages.error(request,'Username is already exist..')
                return redirect('signup')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email already exist..')
                    return redirect('signup')
                else:
                    user=User.objects.create_user(first_name=fn,last_name=ln,username=un,password=pass1)
                    user.save()
                    messages.success(request,'Signup successfully')
                    return redirect('login')
        else:
            messages.error(request,'password does not match..')
            return redirect('signup')

    return render(request,'myaccount/signup.html')
 
def login(request):
    if request.method=='POST':
        un=request.POST.get('uname')
        password=request.POST.get('pass')
        user=auth.authenticate(username=un,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'Login Sucessfully')
            return redirect('dashboard')
        else:
            messages.success(request,'username or password not valid')
            return redirect('login')

    return render(request,'myaccount/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def dashboard(request):
    data=Student_details.objects.all()

    context={
        'students':data
    }
    return render(request,'myaccount/dashboard.html',context)

def singlestudentdetails(request,reg):
     student=Student_details.objects.get(reg_no=reg)

     context={
         'student':student
     }
     if request.method=='POST':
            name=request.POST.get('name')
            city=request.POST.get('city')
            email=request.POST.get('email')
            degree=request.POST.get('degree')
            percentage=request.POST.get('percentage')
            course=request.POST.get('course')
            fee=request.POST.get('fee')
            student=Student_details.objects.get(reg_no=reg)
            student.name=name
            student.city=city
            student.email=email
            student.degree=degree
            student.percentage=percentage
            student.course=course
            student.fee=fee
            student.save()
            return redirect('dashboard')

     return render(request,'myaccount/singlestudentdetails.html',context)

def delete(request,reg):
    student=Student_details.objects.get(reg_no=reg)
    student.delete()

    return redirect('dashboard')