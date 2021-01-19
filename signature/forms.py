from django.forms import ModelForm
from .models import EmployeeInfo
from django import forms

class SignatureForm(ModelForm):
    class Meta:
        model = EmployeeInfo

        fields = ['employee_first_name', 'employee_last_name', 'employee_title', 
        'employee_area_code','employee_phone_number', 'employee_pronoun_list', 'employee_pronoun_other', 
        'employee_address', 
        'employee_address_other1', 'employee_address_other2', 'employee_zoomid', 'employee_profile_pic']
        
        widgets = {
            'employee_pronoun_list': forms.RadioSelect,
            'employee_address': forms.RadioSelect,
        }