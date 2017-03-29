from __future__ import unicode_literals
from django.db import models
from django.forms import extras
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
TITLE_CHOICES = (
    ('ND', 'Not Done'),
    ('D', 'Done'),
)

class ApplianceName(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    appliance = models.CharField(max_length=100)
    def __str__(self):
        return str(self.user.id)+" - "+str(self.user)+" - "+self.appliance

class Usage(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    app_id=models.ForeignKey(ApplianceName, on_delete=models.CASCADE)
    use=models.IntegerField(max_length=10,default=0)
    recordtime=models.DateTimeField()
    def __str__(self):
        return str(self.app_id)+" - "+str(self.use)+" - "+str(self.recordtime)

class Complaint(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    complaint_num = models.AutoField(primary_key=True)
    comp = models.CharField(max_length=1000)
    status = models.CharField(max_length=10,choices=TITLE_CHOICES,default='ND')
    def __str__(self):
        return str(self.user.id)+" - "+str(self.user)+" - "+str(self.user.profile.address)+" - "+self.comp+" - "+self.status

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=1000, blank=True)
    def __str__(self):
        return str(self.user.id)+" - "+str(self.user)+" - "+self.address

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()