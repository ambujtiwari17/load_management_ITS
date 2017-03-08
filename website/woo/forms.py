from django import forms
from .models import *
from django.utils.translation import ugettext_lazy as _

class Complaintform(forms.ModelForm):
    class Meta:
        model=Complaint
        fields = ['complaint_num', 'comp', 'status']
        labels = {
            'complaint_num': _('Complaint Number'),
            'comp': _('Complaint'),
            'status': _('Status'),
        }

class Usageform(forms.ModelForm):
    class Meta:
        model=Usage
        fields = ['app_id', 'use', 'recordtime']
        labels = {
            'app_id': _('Select Appliance'),
            'use': _('Units Used'),
            'recordtime': _('Recording Date and Time'),
        }

class Applianceform(forms.ModelForm):
    class Meta:
        model=ApplianceName
        fields = ['appliance']
        labels = {
            'appliance': _('Appliance Name'),
        }