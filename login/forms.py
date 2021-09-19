from django import forms
from blogger.models import blogger
class LoginForm(forms.ModelForm):

    class Meta:
        model = blogger
        fields = ['email','password']
        widgets = {'password': forms.PasswordInput(),}   