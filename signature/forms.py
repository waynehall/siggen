from django.forms import ModelForm
from .models import EmployeeInfo


class SignatureForm(ModelForm):
    class Meta:
        model = EmployeeInfo
        fields = ['employee_first_name', 'employee_last_name', 'employee_title', 'employee_area_code','employee_phone_number', 'employee_pronoun_list', 'employee_address1', 'employee_address2', 'employee_zoomid', 'employee_profile_pic']