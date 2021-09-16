from django import forms
from .models import post
class CreatPostForm(forms.ModelForm):

    class Meta:
        model = post
        exclude = ["date", "blogger_id"]
          
 
    