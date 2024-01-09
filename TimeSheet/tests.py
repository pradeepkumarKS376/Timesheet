import datetime

from django.db.models import Count
from django.db.models import Sum
from models import *
from django.test import TestCase

# Create your tests here.
# week_start = datetime.date.today()
# week_start -= datetime.timedelta(days=(week_start.weekday() + 1) % 7)
# week_end = week_start + datetime.timedelta(days=7)


def Totalhr():
    # Emp_id = request.session['Employee_ID']
    week_start = datetime.date.today()
    week_start -= datetime.timedelta(days=(week_start.weekday() + 1) % 7)
    week_end = week_start + datetime.timedelta(days=7)
    Total_Hours = Empattendancemodule.objects.filter(Employee_id="150067").filter(DATE__gte=week_start,
                                                                                DATE__lte=week_end).aggregate(
        Total_Hours=Sum('HOURS'))
    Total_Hours = str(Total_Hours).split(":")[1].split("}")[0]
    return Total_Hours

Totalhr()