from django import forms
from models import *

class Complaintform(forms.ModelForm):
    class Meta:
        model=Complaint

class Usageform(forms.ModelForm):
    class Meta:
        model=Usage

class Applianceform(forms.ModelForm):
    class Meta:
        model=ApplianceName