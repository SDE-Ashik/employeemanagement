from django import forms
class OperationForm(forms.Form):
    num1 = forms.IntegerField(label="enter  number")
    num2 = forms.IntegerField(label="enter number")
