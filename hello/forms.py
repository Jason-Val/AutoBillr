from django import forms

from .models import Bill 

class BillCreationForm(forms.Form):
    billName = forms.CharField(label='enter name', max_length=100)
    billAmount = forms.CharField(label='Bill Amount', max_length=100)
    billInterval = forms.CharField(label='How Often to Pay', max_length=100)
