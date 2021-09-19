from django import forms
from .models import blogger
class signupForm(forms.ModelForm):

    class Meta:
        model = blogger
        fields = '__all__'
        widgets = {'password': forms.PasswordInput(),}   

   
    