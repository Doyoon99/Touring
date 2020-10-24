from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from touring import settings


# Create your models here.
#class Profile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE, default=timezone.now, null=True)

class Plan(models.Model):
    title = models.CharField(max_length=200)
    departDate = models.DateField(blank=True, default=timezone.now, null=True)
    arriveDate = models.DateField(blank=True, default=timezone.now, null=True)
    password = models.CharField(max_length=200)
    hotel = models.CharField(max_length=200)
    created_at = models.DateTimeField('작성시간', default = timezone.now)
    updated_at = models.DateTimeField('수정시간', default = timezone.now)
    view_count = models.IntegerField(default=0)
    scrap_users = models.ManyToManyField(User, through='Scrap', related_name= 'scrap_plans')
    scrap_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Scrap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.plan.title

