from django.urls import path
from . import views

urlpatterns=[
    path('map/<int:plan_id>', views.map, name='map'),
    path('start/', views.start, name='start'),
    path('plancreate/', views.plancreate, name='plancreate'),
    path('plandelete/<int:plan_id>', views.plandelete, name='plandelete'),
    path('planList/', views.planList, name='planList'),
    path('search/', views.search, name='search'),
    path('map/last/', views.last, name='last'),
    path('scrap/<int:plan_id>', views.scrap, name='scrap'),
    path('scraplist/', views.scraplist, name='scraplist'),
]