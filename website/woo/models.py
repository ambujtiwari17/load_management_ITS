from __future__ import unicode_literals
from django.db import models
from django.forms import extras

TITLE_CHOICES = (
    ('ND', 'Not Done'),
    ('D', 'Done'),
)

class ApplianceName(models.Model):
    appliance = models.CharField(max_length=100)
    def __str__(self):
        return self.appliance

class Usage(models.Model):
    app_id=models.ForeignKey(ApplianceName, on_delete=models.CASCADE)
    use=models.IntegerField(max_length=10,default=0)
    recordtime=models.DateTimeField()
    def __str__(self):
        return str(self.app_id)+" - "+str(self.use)+" - "+str(self.recordtime)

class Complaint(models.Model):
    complaint_num = models.IntegerField(max_length=10,default=1)
    comp = models.CharField(max_length=100)
    status = models.CharField(max_length=10,choices=TITLE_CHOICES,default='ND')
    def __str__(self):
        return self.comp+" - "+self.status
