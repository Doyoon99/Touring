from django.shortcuts import render, get_object_or_404, redirect
from .models import Memo
from tourPlan.models import Plan
from .forms import MemoForm
import tourPlan.views
# Create your views here.

#Memo
def memocreate(request, plan_id):
    plan_detail = get_object_or_404(Plan, pk=plan_id)
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.plan = plan_detail
            memo.save()
            return redirect('map', plan_id=plan_detail.pk)
        else:
            redirect('home')
    else:
        form = MemoForm()
        return render(request, 'map.html', {'form':form, 'plan':plan_detail})

def memoupdate(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    if request.method == 'POST':
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.save()
            return redirect('map', plan_id=memo.plan.pk)
        else:
            redirect('home')
    else:
        form = MemoForm(instance=memo)
        return render(request, 'map.html', {'form':form, 'plan':memo.plan})


def memodelete(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    memo.delete()
    return redirect('map', plan_id=memo.plan.pk)