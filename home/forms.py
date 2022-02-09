from django import forms
from home.models import Customer


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'Address','phone', 'city', 'zipcode', 'state', 'country']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'Address':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
            'State':forms.Select(attrs={'class':'form-control'}),
            'country':forms.TextInput(attrs={'class':'form-control'}),
            
                   
                   }



