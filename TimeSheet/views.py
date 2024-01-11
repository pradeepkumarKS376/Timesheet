import datetime
from django.contrib.auth import logout
from django.shortcuts import render
from .Forms import *
from django.db.models import Sum


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if (Loginmodule.objects.filter(Username=username, Password=password)).exists():
            Emp_id = Loginmodule.objects.values_list('Emp_id', flat=True).get(Username=username)
            request.session['Employee_ID'] = Emp_id
            request.session.set_test_cookie()
            client_details = Baseclientmodule.objects.all().filter(Emp_id=Emp_id)
            Admin_Id = Admin_Ids(Emp_id)
            Totalhrs = Totalhr(Emp_id)
            Empattendancdetails = Sort_week(Emp_id)
            response = render(request, "index.html", {"client_details": client_details, "Empattendancdetails": Empattendancdetails, "Emp_id": Emp_id, "Total_Hours": Totalhrs, "Admin_Id":Admin_Id})
            return response
        else:
            return render(request, 'login-2.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        return render(request, 'login-2.html')


def inserttimesheet_view(request):
    Emp_id = request.session['Employee_ID']
    client_details = Baseclientmodule.objects.all().filter(Emp_id=Emp_id)
    Totalhrs = Totalhr(Emp_id)
    Empattendancdetails = Sort_week(Emp_id)
    Admin_Id = Admin_Ids(Emp_id)
    if request.method == 'POST':
        DATE = request.POST['DATE']
        Client_Id = request.POST['Client_Id']
        Client_Name = request.POST['Client_Name']
        Task_Name = request.POST['Task_Name']
        HOURS = request.POST['HOURS']
        a = Empattendancemodule.objects.create(DATE=DATE, Client_Id=Client_Id, Client_Name=Client_Name, Task_Name=Task_Name, HOURS=HOURS, Employee_id=Emp_id)
        a.save()
        Totalhrs = Totalhr(Emp_id)
        Admin_Id = Admin_Ids(Emp_id)
        return render(request, "index.html", {"client_details": client_details, "Empattendancdetails": Empattendancdetails, "Emp_id": Emp_id, "Total_Hours": Totalhrs, "Admin_Id": Admin_Id})
    else:
        return render(request, "index.html", {"client_details": client_details, "Empattendancdetails": Empattendancdetails, "Emp_id": Emp_id, "Total_Hours": Totalhrs, "Admin_Id": Admin_Id})


def edit_view(request, id):
    Emp_id = request.session['Employee_ID']
    Totalhrs = Totalhr(Emp_id)
    Admin_Id = Admin_Ids(Emp_id)
    Empattendancdetails = Empattendancemodule.objects.all().get(id=id)
    if request.method == 'POST':
        form = EmpattendanceForm(request.POST, instance=Empattendancdetails)
        if form.is_valid():
            form.save()
            Totalhrs = Totalhr(Emp_id)
            client_details = Baseclientmodule.objects.all().filter(Emp_id=Emp_id)
            Empattendancdetail = Sort_week(Emp_id)
            Admin_Id = Admin_Ids(Emp_id)
            if (Admin_Id==Emp_id and Emp_id !=Emp_id):
                Adminref = Baseclientmodule.objects.all().values_list('Emp_id', flat=True).distinct().filter(
                    Admin_Id=Emp_id).order_by('Emp_id')
                return render(request, "AdminRef.html",
                              {"client_details": client_details, "Empattendancdetails": Empattendancdetail,
                               "Emp_id": Emp_id, "Total_Hours": Totalhrs, "Admin_Id": Admin_Id, "Adminref": Adminref})
            else:
                return render(request, "index.html", {"client_details": client_details, "Empattendancdetails": Empattendancdetail, "Emp_id": Emp_id, "Total_Hours": Totalhrs, "Admin_Id":Admin_Id})
    return render(request, "Update.html",
                  {"Empattendancdetails": Empattendancdetails, "Emp_id": Emp_id, "Total_Hours": Totalhrs, "Admin_Id":Admin_Id})


def del_view(request, id):
    Emp_id = request.session['Employee_ID']
    Empattendancdetails = Empattendancemodule.objects.all().filter(id=id)
    Empattendancdetails.delete()
    Totalhrs = Totalhr(Emp_id)
    client_details = Baseclientmodule.objects.all().filter(Emp_id=Emp_id)
    Empattendancdetail = Sort_week(Emp_id)
    Admin_Id = Admin_Ids(Emp_id)
    if (Admin_Id==Emp_id and Emp_id !=Emp_id):
        Adminref = Baseclientmodule.objects.all().values_list('Emp_id', flat=True).distinct().filter(
            Admin_Id=Emp_id).order_by('Emp_id')
        return render(request, "AdminRef.html",
                      {"client_details": client_details, "Empattendancdetails": Empattendancdetail,
                       "Emp_id": Emp_id, "Total_Hours": Totalhrs, "Admin_Id": Admin_Id, "Adminref": Adminref})
    return render(request, "index.html",
                  {"client_details": client_details, "Empattendancdetails": Empattendancdetail, "Emp_id": Emp_id, "Total_Hours": Totalhrs, "Admin_Id":Admin_Id})


def logout_view(request):
    try:
        del request.session["Employee_ID"]
        logout(request)
    except KeyError:
        pass
    return render(request, "Login-2.html")


def Totalhr(Emp_id):
    a = Filter_Date()
    week_start = a[0]
    week_end = a[1]
    Total_Hours = Empattendancemodule.objects.filter(Employee_id=Emp_id).filter(DATE__gte=week_start,
                                                                                DATE__lte=week_end).aggregate(
        Total_Hours=Sum('HOURS'))
    Total_Hours = str(Total_Hours).split(":")[1].split("}")[0]
    if Total_Hours.strip() == 'None':
        Total_Hours = 0
    else:
        Total_Hours = int(Total_Hours)
    return Total_Hours


def Sort_week(Emp_id):
    a = Filter_Date()
    week_start = a[0]
    week_end = a[1]
    Empattendancdetail = (Empattendancemodule.objects.all().filter(Employee_id=Emp_id).filter(DATE__gte=week_start,
                                                                                             DATE__lte=week_end).order_by(
        'DATE'))
    return Empattendancdetail


def Filter_Date():
    week_start = datetime.date.today()
    week_start -= datetime.timedelta(days=(week_start.weekday() + 1) % 7)
    week_end = week_start + datetime.timedelta(days=7)
    return (week_start,week_end)


def Admin_Ids(Emp_id):
    Admin_Id = Baseclientmodule.objects.values_list('Admin_Id', flat=True).distinct().get(Emp_id=Emp_id)
    return Admin_Id


def AdminRef_view(request):
    Emp_id = request.session['Employee_ID']
    client_details = Baseclientmodule.objects.all().filter(Admin_Id=Emp_id)
    Totalhrs = Totalhr(Emp_id)
    Empattendancdetails = Sort_week(Emp_id)
    Admin_Id = Admin_Ids(Emp_id)
    Adminref = Baseclientmodule.objects.all().values_list('Emp_id', flat=True).distinct().filter(Admin_Id=Emp_id).order_by('Emp_id')
    if request.method == 'POST':
        Employee_ID = request.session['Employee_ID']
        Emp_id = request.POST['Emp_id']
        Empattendancdetails = Empattendancemodule.objects.all().filter(Employee_id=Emp_id)
        Totalhrs = Totalhr(Emp_id)
        Admin_Id = Admin_Ids(Emp_id)
        return render(request, "AdminRef.html", {"client_details": client_details, "Empattendancdetails": Empattendancdetails, "Emp_id": Employee_ID, "Total_Hours": Totalhrs, "Adminref": Adminref, "Admin_Id": Admin_Id})
    else:
        return render(request, "AdminRef.html", {"client_details": client_details, "Empattendancdetails": Empattendancdetails, "Emp_id": Emp_id, "Total_Hours": Totalhrs, "Adminref": Adminref, "Admin_Id": Admin_Id})

