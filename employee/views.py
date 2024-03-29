from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
from employee.forms import RegistrationForm, LoginForm, EmployeeForm
from django.contrib import messages


# Create your views here.

# def index(request):
#     return render(request, "home.html")
#
#
#
# def login(request):
#     return render(request, "login.html")


class IndexView(View):
    def get(self, request):
        return render(request, "home.html")


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        print(request.POST.get("u_name"))
        print(request.POST.get("pwd"))
        print("successful")
        return render(request, "login.html")


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, "registration.html", {"form": form})

    def post(self, request):
        print(request.POST.get("f_name"))
        print(request.POST.get("l_name"))
        print(request.POST.get("e_mail"))
        print(request.POST.get("u_name"))
        print(request.POST.get("pwd"))
        return redirect("login")


class EmployeeCreateView(View):
    form_class = EmployeeForm
    template_name = "emp-add.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        print(request.POST)
        if form.is_valid():
            print("cleaned_data")
            print(form.cleaned_data.get("eid"))
            print(form.cleaned_data.get("employee_name"))
            print(form.cleaned_data.get("designation"))
            print(form.cleaned_data.get("salary"))
            print(form.cleaned_data.get("experience"))
            print(form.cleaned_data.get("email"))
            messages.success(request, "profile has been created")
            return redirect("emp-add")
        else:
            messages.error(request, "profile adding failed")
            return render(request, self.template_name, {"form": form})
