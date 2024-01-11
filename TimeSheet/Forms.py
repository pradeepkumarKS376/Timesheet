from django import forms
from .models import *
class BaseclientForm(forms.ModelForm):
    class Meta:
        model = Baseclientmodule
        fields = "__all__"


class LoginForm(forms.ModelForm):
    class Meta:
        model = Loginmodule
        fields = "__all__"


class EmpattendanceForm(forms.ModelForm):
    class Meta:
        model = Empattendancemodule
        fields = "__all__"