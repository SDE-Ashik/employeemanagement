from django import forms


class MathForm(forms.Form):
    num1 = forms.IntegerField(label="enter number")
    num2 = forms.IntegerField(label="enter number")

    def clean(self):
        clean_data = super().clean()
        n1 = clean_data.get("num1")
        n2 = clean_data.get("num2")
        if n1 < 0:
            msg = "Invalid number"
            self.add_error("num1", msg)
        if n2 < 0:
            msg = "Invalid Number"
            self.add_error("num2", msg)
