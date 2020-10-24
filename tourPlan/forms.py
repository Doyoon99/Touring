from django import forms
from .models import Plan

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['title', 'hotel','departDate','arriveDate', 'password']
        widgets = {
            'title' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'required' : False,
                    'placeholder' : '필수 입력칸입니다.', 
                }
            ),
            'hotel' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',   
                    'required' : False, 
                    'placeholder' : '필수 입력칸입니다.',
                }
                
            ),

            'departDate' : forms.DateInput(
                attrs = {
                    'class' : 'form-control',
                    'type' : 'date',
                }
            ),

            'arriveDate' : forms.DateInput(
                attrs = {
                    'class' : 'form-control',
                    'type' : 'date',
                }
            ),
            'password' : forms.TextInput(
                attrs = {
                    'required' : False,
                    'placeholder' : '4자리 숫자로 입력해주세요.', 
                    'class' : 'form-control',
                }
            ),
        }   
        labels = {
            'title': '여행 이름',
            'hotel': '숙소',
            'arriveDate': '오는 날짜',
            'departDate': '가는 날짜',
            'password' : '게시글 비밀번호',
        }
