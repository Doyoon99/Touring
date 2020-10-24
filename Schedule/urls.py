from django.urls import path
from . import views


urlpatterns = [
    path('schedulecreate/<int:plan_id>', views.schedulecreate, name='schedulecreate'),
    path('scheduleupdate/<int:schedule_id>', views.scheduleupdate, name='scheduleupdate'),
    path('scheduledelete/<int:schedule_id>', views.scheduledelete, name='scheduledelete'),
]
    