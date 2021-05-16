from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','email','cpf',]
        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Customer Name'}),
            'email':forms.TextInput(attrs={'placeholder':'Customer Email'}),
            'cpf':forms.TextInput(attrs={'placeholder':'Customer CPF'})
        }