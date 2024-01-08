import datetime

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from .models import *
from .Forms import *

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if (Loginmodule.objects.filter(Username=username, Password=password)).exists():
            Emp_id = Loginmodule.objects.values_list('Emp_id', flat=True).get(Username=username)
            request.session['Employee_ID'] = Emp_id
            request.session.set_test_cookie()
            client_details = Baseclientmodule.objects.all().filter(Emp_id=Emp_id)
            Empattendancdetails = Empattendancemodule.objects.all().filter(Employee_id=Emp_id).filter(DATE=datetime.date.today())
            response =  render(request, "index.html", {"client_details": client_details,"Empattendancdetails":Empattendancdetails,"Emp_id":Emp_id})
            return response
        else:
            return render(request, 'login-2.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        return render(request, 'login-2.html')


def logout_view(request):
    try:
        del request.session["Employee_ID"]
        logout(request)
    except KeyError:
        pass
    return render(request,"Login-2.html")


def inserttimesheet_view(request):

    Emp_id = request.session['Employee_ID']
    client_details = Baseclientmodule.objects.all().filter(Emp_id=Emp_id)
    Empattendancdetails = Empattendancemodule.objects.all().filter(Employee_id=Emp_id).filter(DATE=datetime.date.today())
    if request.method == 'POST':
        DATE = request.POST['DATE']
        Client_Id = request.POST['Client_Id']
        Client_Name = request.POST['Client_Name']
        Task_Name = request.POST['Task_Name']
        HOURS = request.POST['HOURS']
        a = Empattendancemodule.objects.create(DATE=DATE,Client_Id=Client_Id,Client_Name=Client_Name,Task_Name=Task_Name,HOURS=HOURS,Employee_id=Emp_id)
        a.save()
        return render(request, "index.html", {"client_details": client_details,"Empattendancdetails":Empattendancdetails,"Emp_id":Emp_id})
    else:
        return render(request, "index.html", {"client_details": client_details,"Empattendancdetails":Empattendancdetails,"Emp_id":Emp_id})


def edit_view(request,id):
    Emp_id = request.session['Employee_ID']
    Empattendancdetails = Empattendancemodule.objects.all().get(id=id)
    if request.method == 'POST':
        form = EmpattendanceForm(request.POST, instance=Empattendancdetails)
        DATE = request.POST['DATE']
        print(DATE)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            client_details = Baseclientmodule.objects.all().filter(Emp_id=Emp_id)
            Empattendancdetail = Empattendancemodule.objects.all().filter(Employee_id=Emp_id).filter(DATE=datetime.date.today())
            return render(request, "index.html",{"client_details": client_details,"Empattendancdetails": Empattendancdetail, "Emp_id": Emp_id})
        # else:
        #     print("ppp")
    return render(request, "Update.html",
                  {"Empattendancdetails": Empattendancdetails, "Emp_id": Emp_id})

def del_view(request,id):
    Emp_id = request.session['Employee_ID']
    Empattendancdetails = Empattendancemodule.objects.all().filter(id=id)
    Empattendancdetails.delete()
    client_details = Baseclientmodule.objects.all().filter(Emp_id=Emp_id)
    Empattendancdetail = Empattendancemodule.objects.all().filter(Employee_id=Emp_id).filter(
        DATE=datetime.date.today())
    return render(request, "index.html",
                  {"client_details": client_details, "Empattendancdetails": Empattendancdetail, "Emp_id": Emp_id})
