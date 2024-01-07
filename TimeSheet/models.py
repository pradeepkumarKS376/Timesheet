from django.db import models
import sqlite3


# Create your models here.
class Empmodel(models.Model):
    Empcode = models.CharField(max_length=254, default=None, null=False,primary_key=True)
    EmpName = models.CharField(max_length=254, default=None, null=False)
    objects = models.Manager()

    class Meta:
        db_table = "Emp"
class Baseclientmodule(models.Model):
    Task_Name = models.CharField(max_length=254, default=None, null=False)
    Client_Name = models.CharField(max_length=254, default=None, null=False)
    Client_Id = models.CharField(max_length=254, default=None, null=False)
    Admin_Id = models.CharField(max_length=254, default=None, null=False)
    Emp_id = models.ForeignKey(Empmodel, null=True, on_delete=models.CASCADE)
    objects = models.Manager()

    class Meta:
        # ordering = ["Client_Id", "Admin_Id"]
        db_table = "Baseclient"

    def __str__(self):
        self.con = sqlite3.connect("db.sqlite3")
        self.cur = self.con.cursor()
        return f"{self.Emp_id}"
class Loginmodule(models.Model):
    Emp_id = models.ForeignKey(Empmodel, null=True, on_delete=models.CASCADE)
    Username = models.CharField(max_length=254, default=None, null=False)
    Password = models.CharField(max_length=254, default=None, null=False)
    objects = models.Manager()

    class Meta:
        db_table = "Login"
    def __str__(self):
        return self.Emp_id
class Empattendancemodule(models.Model):
    Employee_id = models.CharField(max_length=254, default=None, null=False)
    DATE = models.DateField(max_length=254, default=None, null=False)
    Client_Name = models.CharField(max_length=254, default=None, null=False)
    Client_Id = models.CharField(max_length=254, default=None, null=False)
    Task_Name = models.CharField(max_length=254, default=None, null=False)
    HOURS = models.CharField(max_length=254, default=None, null=False)
    # TOTALHOURS = models.CharField(max_length=254, default=None, null=False)