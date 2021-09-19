from django import forms
from blogger.models import blogger

class SignupForm(forms.ModelForm):
    class Meta:
        model = blogger
        fields = '__all__'
        widgets = {'password': forms.PasswordInput(),}   

   
    