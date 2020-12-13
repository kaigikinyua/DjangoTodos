from django import forms
from django.contrib.auth.models import User
class LoginForm(forms.Form):
    username=forms.CharField(required=True)
    password=forms.CharField(required=True)

class SignUpForm(forms.Form):
    class Meta:
        model=User
        
    username=forms.CharField(required=True)
    email=forms.EmailField(required=True)
    password=forms.CharField(required=True)
    c_pass=forms.CharField(required=True)

    def pass_match(self):
        if(self.data["password"]!=self.data["c_pass"]):
            return False
            #raise ValidationError("Passwords do not match")
        #return self.cleaned_data
        return True

class TodoForm(forms.Form):
    todo=forms.CharField(required=True)
    