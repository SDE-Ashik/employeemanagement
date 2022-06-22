from django.shortcuts import render
from django.views.generic import View
from mathcalculation.forms import MathForm
# from calculator.forms import OperationForm

# Create your views here.

class AddView(View):
    def get(self, request):
        form = MathForm()
        return render(request, "add1.html", {"form": form})
    def post(self, request):
        form = MathForm(request.POST)
        if not form.is_valid():
            return render(request,"add1.html", {"form": form})
        n1 = form.cleaned_data.get("num1")
        n2 = form.cleaned_data.get("num2")
        result = n1 + n2
        return render(request,"add1.html",{"addres":result})



class SubView(View):
    def get(self,request):
        form = MathForm()
        return render(request,"sub.html",{"form":form})
    def post(self, request):
        form = MathForm(request.POST)
        if not form.is_valid():
            return render(request,"sub.html",{"form":form})
        n1 = form.cleaned_data.get("num1")
        n2 = form.cleaned_data.get("num2")
        result = n1-n2
        return render(request,"sub.html",{"subres":result})

class MulView(View):
    def get(self, request):
        formm = MathForm()
        return render(request,"mul1.html",{"form":formm})
    def post(self,request):
        formm = MathForm(request.POST)
        if not formm.is_valid():
            return render(request,"mul1.html", {"form":formm})
        n1 = formm.cleaned_data.get("num1")
        n2 = formm.cleaned_data.get("num2")
        result = n1* n2
        return render(request,"mul1.html", {"mures":result})

class DiviForm(View):
    def get(self,request):
        formm = MathForm()
        return render(request,"div1.html",{"form": formm})
    def post(self, request):
        formm = MathForm(request.POST)
        if not formm.is_valid():
            return render(request,"div1.html",{"form":formm})
        n1 = formm.cleaned_data.get("num1")
        n2 = formm.cleaned_data.get("num2")
        result = n1 / n2
        return render(request,"div1.html",{"div":result, "form": formm})
