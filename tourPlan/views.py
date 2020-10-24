from django.shortcuts import render, get_object_or_404, redirect, redirect, HttpResponseRedirect
from .models import Plan, Scrap
from .forms import PlanForm
from django.core.paginator import Paginator

# Create your views here.

def map(request, plan_id):
    plan_detail = get_object_or_404(Plan, pk = plan_id)
    plan_object = Plan.objects.get(id=plan_id)
    plan_object.view_count = plan_object.view_count+1
    plan_object.save()
    return render(request, 'map.html', {'plan':plan_detail})

def planList(request):
    plans = Plan.objects
    sort = request.GET.get('sort','')
    plan_list = Plan.objects.all()
    if sort == 'scrap':
        plan_list = Plan.objects.all().order_by('-scrap_count', '-created_at')
    elif sort == 'view':
        plan_list = Plan.objects.all().order_by('-view_count', '-created_at')
    elif sort == 'date':
        plan_list = Plan.objects.all().order_by('-created_at')
    elif sort == 'writedate':
        plan_list = Plan.objects.all().order_by('created_at')
    secret = Plan.password
    paginator = Paginator(plan_list,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'planList.html', {'plans':plans, 'posts':posts })    
   
        
def start(request):
    plans = Plan.objects
    return render(request, 'start.html', {'plans':plans})

def plancreate(request):
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.save()
            return redirect('planList')
    else:
        form = PlanForm()
        return render(request, 'start.html', {'form':form})


def plandelete(request, plan_id):
    plan = get_object_or_404(Plan, pk = plan_id)
    plan.delete()
    return redirect('planList')

def search(request):
    plan_object = Plan.objects.all()
    query = request.GET.get('query','')
    page = request.GET.get('page')
    paginator = Paginator(plan_object.filter(title__icontains= query), 10)
    searches = paginator.get_page(page)
    if query : 
        plan_object = plan_object.filter(title__icontains= query)
    return render(request, 'search.html', {'search':plan_object, 'query':query, 'searches':searches})
    

def last(request):
    return render(request,'last.html')

def scrap(request, plan_id):
    plan = get_object_or_404(Plan, pk=plan_id)
    user = request.user
    scrapped = Scrap.objects.filter(user=request.user, plan=plan)

    if not scrapped:
        Scrap.objects.create(user=request.user, plan=plan)
        plan.scrap_count += 1
        plan.save()
    else:
        scrapped = Scrap.objects.get(user=request.user, plan=plan)
        plan.scrap_count -= 1
        plan.save()
        scrapped.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))



def scraplist(request):
    scraps = Scrap.objects.filter(user=request.user)
    user = request.user
    paginator = Paginator(scraps,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'scraplist.html', {'scraps':scraps, 'posts':posts, 'user':user})