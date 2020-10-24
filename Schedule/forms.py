from django import forms
from .models import Schedule

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['date', 'time','schedule']
        widgets = {

            'date': forms.DateInput(
                attrs={
                    'class':'form-control',
                    'type': 'date',
                }
            ),  

            'time': forms.DateInput(
                attrs={
                    'class':'form-control',
                    'type': 'time',
                }
            ), 

            'schedule': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows':'5',
                }
            ), 
        }