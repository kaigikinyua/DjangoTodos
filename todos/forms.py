from django import forms

class LoginForm(forms.Form):
    email=forms.EmailField(required=True)
    password=forms.CharField(required=True)

class SignUpForm(forms.Form):
    username=forms.CharField(required=True)
    email=forms.EmailField(required=True)
    password=forms.CharField(required=True)
    conf_pass=forms.CharField(required=True)

    def pass_match(self):
        if(self.data["password"]!=self.data["conf_pass"]):
            return False
            #raise ValidationError("Passwords do not match")
        #return self.cleaned_data
        return True

class TodoForm(forms.Form):
    todo=forms.CharField(required=True)
    