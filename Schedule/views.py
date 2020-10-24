from django.shortcuts import render, get_object_or_404, redirect
from .models import Schedule
from tourPlan.models import Plan
from .forms import ScheduleForm
import tourPlan.views

# Create your views here.

#Schedule
def schedulecreate(request, plan_id):
    form_s = ScheduleForm(request.POST)
    plan_detail = get_object_or_404(Plan, pk=plan_id)
    if request.method == 'POST':
        form_s = ScheduleForm(request.POST)
        if form_s.is_valid():
            schedule = form_s.save(commit=False)
            schedule.plan = plan_detail
            schedule.save()
            return redirect('map', plan_id=plan_detail.pk)
        else:
            redirect('home')
    else:
        form_s = ScheduleForm(request.POST)
        return render(request, 'map.html', {'form_s':form_s, 'plan':plan_detail})

def scheduleupdate(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    if request.method == 'POST':
        form_s = ScheduleForm(request.POST)
        if form_s.is_valid():
            schedule = form_s.save(commit=False)
            schedule.save()
            return redirect('map', plan_id=schedule.plan.pk)
        else:
            redirect('home')
    else:
        form_s = ScheduleForm(instance=schedule)
        return render(request, 'map.html', {'form_s':form_s, 'plan':schedule.plan})


def scheduledelete(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    schedule.delete()
    return redirect('map', plan_id=schedule.plan.pk)