from django import forms
from .models import blogger
class signupForm(forms.ModelForm):

    class Meta:
        model = blogger
        fields = '__all__'
        widgets = {'password': forms.PasswordInput(),}   

class loginForm(forms.ModelForm):

    class Meta:
        model = blogger
        fields = ['email','password']
        widgets = {'password': forms.PasswordInput(),}   
    