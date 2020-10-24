from django.db import models
from django.utils import timezone
import datetime
from tourPlan.models import Plan

# Create your models here.

class Schedule(models.Model):
    class Meta:
        ordering = ['date', 'time']
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, default=None, blank=True, null=True)
    schedule = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateField('날짜', default=timezone.now, blank=True, null=True)
    time = models.TimeField('시간', auto_now=False, default=timezone.now, blank=True, null=True, auto_now_add = False)
    created_at = models.DateTimeField('작성시간', default = timezone.now)
    updated_at = models.DateTimeField('수정시간', default = timezone.now)
    
    def __str__(self):
        return self.schedule        
