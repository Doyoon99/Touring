from django.urls import path
from . import views

urlpatterns = [
    path('memocreate/<int:plan_id>', views.memocreate, name='memocreate'),
    path('memoupdate/<int:memo_id>', views.memoupdate, name='memoupdate'),
    path('memodelete/<int:memo_id>', views.memodelete, name='memodelete'),
]