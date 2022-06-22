from django import forms


class RegistrationForm(forms.Form):
    f_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"FIRST NAME"}))
    l_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "LAST NAME"}))
    e_mail = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder":"EMAIL"}))
    u_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "USER NAME"}))
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder":"PASSWORD"}))


class LoginForm(forms.Form):
    u_name = forms.CharField(label="enter your user name")
    pwd = forms.CharField(label="enter your password")


class EmployeeForm(forms.Form):
    eid = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control" , "placeholder":"enter eid"}))
    employee_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    designation = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    salary = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    experience = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))

    def clean(self):
        cleaned_data = super().clean()
        exp = cleaned_data.get("experience")
        sal = cleaned_data.get("salary")
        if exp < 0:
            msg = "INVALID EXPERIENCE"
            self.add_error("experience", msg)
        if  sal< 0:
            msg = "SALARY ALWAYS POSTIVE "
            self.add_error("salary", msg)