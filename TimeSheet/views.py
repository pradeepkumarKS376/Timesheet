import datetime

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from .models import *

def login_view(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        global Emp_ids
        def Emp_ids():
            global Emp_id
            Emp_id = Loginmodule.objects.values_list('Emp_id', flat=True).get(Username=username)
        Emp_ids()
        if (Loginmodule.objects.filter(Username=username, Password=password)).exists():
            client_details = Baseclientmodule.objects.all().filter(Emp_id=Emp_id)
            Empattendancdetails = Empattendancemodule.objects.all().filter(Employee_id=Emp_id).filter(DATE=datetime.date.today())
            # request.session['session_name'] = a.Username
            return render(request, "index.html", {"client_details": client_details,"Empattendancdetails":Empattendancdetails})
        else:
            return render(request, 'login-2.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        return render(request, 'login-2.html')


def logout_view(request):
        logout(request)
        return render(request,"Login-2.html")


def inserttimesheet_view(request):
    Emp_ids()
    client_details = Baseclientmodule.objects.all().filter(Emp_id=Emp_id)
    Empattendancdetails = Empattendancemodule.objects.all().filter(Employee_id=Emp_id).filter(
        DATE=datetime.date.today())
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

