from django.shortcuts import render
from django.views.generic import View
from calculator.forms import OperationForm


# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, "cal_home.html")


class AdddView(View):
    def get(self, request):
        form = OperationForm()
        return render(request, "add.html", {"form": form})

    def post(self, request):
        # n1 = int(request.POST.get("num1"))
        # n2 = int(request.POST.get("num2"))
        # result = n1 + n2
        # print(result)

        form = OperationForm(request.POST)
        if form.is_valid():
            n1 = form.cleaned_data.get("num1")
            n2 = form.cleaned_data.get("num2")
            result = n1 + n2
            print(form.cleaned_data)

            return render(request, "add.html", {"res": result, "form": form}, )
        else:
            return render(request, "add.html", {"form": form})


class SubView(View):
    def get(self, request):
        form = OperationForm()
        return render(request, "sub.html", {"form": form})

    def post(self, request):
        # n1 = request.POST.get("num1")
        # n2 = request.POST.get("num2")
        # result = int(n1) - int(n2)
        form = OperationForm(request.POST)
        if not form.is_valid():
            return render(request, "sub.html", {"form": form})
        n1 = form.cleaned_data.get("num1")
        n2 = form.cleaned_data.get("num2")
        result = n1 - n2
        return render(request, "sub.html", {"subres": result})


class MulView(View):
    def get(self, request):
        form = OperationForm()
        return render(request, "mul.html", {"form": form})

    def post(self, request, result=None):
        # n1 = int(request.POST.get("num1"))
        # n2 = int(request.POST.get("num2"))
        # result = n1 * n2
        form = OperationForm(request.POST)
        if not form.is_valid():
            return render(request,"mul.html",{"form":form})
        n1 = form.cleaned_data.get("num1")
        n2 = form.cleaned_data.get("num2")
        mul = n1 * n2

        return render(request, "mul.html", {"mulres": mul})


class DivView(View):
    def get(self, request):
        form = OperationForm()
        return render(request, "div.html", {"form": form})

    def post(self, request):
        form = OperationForm(request.POST)
        if not form.is_valid():
            return render(request, "div.html", {"form": form})
        n1 = form.cleaned_data.get("num1")
        n2 = form.cleaned_data.get("num2")
        # n1 = int(request.POST.get("num1"))
        # n2 = int(request.POST.get("num2"))
        result = n1 / n2
        return render(request, "div.html", {"divres": result, "form": form})


class CubeView(View):
    def get(self, request):
        return render(request, "cube.html")

    def post(self, request):
        n1 = int(request.POST.get("num1"))

        result = n1 ** 3
        return render(request, "cube.html", {"cures": result})


class SquareView(View):
    def get(self, request):
        return render(request, "square.html")

    def post(self, request):
        n1 = int(request.POST.get("num1"))
        result = n1 ** 2
        return render(request, "square.html", {"sqres": result})


class FactView(View):
    def get(self, request):
        return render(request, "fact.html")

    def post(self, request):
        n1 = int(request.POST.get("num1"))
        fact = 1
        for start in range(1, n1 + 1):
            fact = fact * start
        result = fact
        return render(request, "fact.html", {'factres': result})


class CountView(View):
    def get(self, request):
        return render(request, "wordcount.html")

    def post(self, request):
        word = request.POST.get("word")
        words = word.split(" ")
        wc = {}
        for w in words:
            if w in wc:
                wc[w] += 1
            else:
                wc[w] = 1
        for key, value in wc.items():
            print(key, value)

        return render(request, "wordcount.html", {"word": wc})


class PrimeView(View):
    def get(self, request):
        return render(request, "prime.html")

    def post(self, request):
        init = int(request.POST.get("init"))
        final = int(request.POST.get("final"))
        prime = []
        for i in range(init, final + 1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime.append(i)

        print(prime)
        return render(request, "prime.html", {"primeres": prime})
