from django import forms
from .models import PanCard

class PanCardForm(forms.ModelForm):
    class Meta:
        model = PanCard
        fields = '__all__'

        widgets = {
            'fname': forms.TextInput(attrs={'class':'form-control'}),
            'lname': forms.TextInput(attrs={'class':'form-control'}),
            'mobile_number': forms.NumberInput(attrs={'class':'form-control'}),
            'pan_no': forms.TextInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'gender': forms.Select(attrs={'class':'form-control'})
        }
        labels={
            'dob':"Date Of Birth",
            'pan_no':"Permanent Account Number",
        }