from django import forms
from .models import *
class BaseclientForm(forms.ModelForm):
    class Meta:
        model = Baseclientmodule
        fields = "__all__"