from typing import Any
from django import forms
from .models import Student
from .models import Standard
from .models import Subject


class StudentForms(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class StandardForms(forms.ModelForm):
    subject = forms.CharField(max_length=256)

    class Meta:
        model = Standard
        fields = ["standard", "subject"]
