from django import forms
class RegistrationForm(forms.Form):
    f_name = forms.CharField(label="Enter first name")
    l_name = forms.CharField(label="Enter last name")
    e_mail = forms.EmailField(label="Enter your email")
    u_name = forms.CharField(label="Enter your Username")
    pwd = forms.CharField(label="Enter your password")

class LoginForm(forms.Form):
    u_name = forms.CharField(label="enter your user name")
    pwd = forms.CharField(label="enter your password")