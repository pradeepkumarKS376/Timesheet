import datetime

from django.test import TestCase

# Create your tests here.
week_start = datetime.date.today()
week_start -= datetime.timedelta(days=(week_start.weekday() + 1) % 7)
week_end = week_start + datetime.timedelta(days=7)
