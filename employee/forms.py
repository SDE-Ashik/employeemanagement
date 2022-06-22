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


class EmployeeForm(forms.Form):
    eid = forms.CharField()
    employee_name = forms.CharField()
    designation = forms.CharField()
    salary = forms.IntegerField()
    email = forms.EmailField()
    experience = forms.IntegerField()

    def clean(self):
        cleaned_data = super().clean()
        exp = cleaned_data.get("experience")
        if exp < 0:
            msg = "INVALID EXPERIENCE"
            self.add_error("experience", msg)
