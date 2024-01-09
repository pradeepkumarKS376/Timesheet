import datetime


def Filter_Date():
    week_start = datetime.date.today()
    week_start -= datetime.timedelta(days=(week_start.weekday() + 1) % 7)
    week_end = week_start + datetime.timedelta(days=7)
    return (week_start,week_end)

a = Filter_Date()
print(a[0])