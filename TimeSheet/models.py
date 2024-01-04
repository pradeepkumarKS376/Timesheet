from django.db import models
import sqlite3


# Create your models here.
class Baseclientmodule(models.Model):
    Project_Name = models.CharField(max_length=254, default=None, null=False)
    Account = models.CharField(max_length=254, default=None, null=False)
    Project_ID = models.CharField(max_length=254, default=None, null=False)
    Admin = models.CharField(max_length=254, default=None, null=False)
    objects = models.Manager()

    class Meta:
        ordering = ["Account", "Admin"]
        db_table = "Baseclient"
        #fields = '__all__'

    def __str__(self):
        self.con = sqlite3.connect("Resume.sqlite3")
        self.cur = self.con.cursor()
        return f"{self.Project_ID}"

