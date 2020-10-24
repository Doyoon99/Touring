from django.db import models
from django.utils import timezone
import datetime
from tourPlan.models import Plan

# Create your models here.
class Memo(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, default=None, blank=True, null=True)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField('작성시간', default = timezone.now)
    updated_at = models.DateTimeField('수정시간', default = timezone.now)

    def __str__(self):
        return self.content