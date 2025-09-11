# from django.http import HttpResponse
# from django.shortcuts import render


# def index(request):
#     return render(request, "work05_1/index.html")
# def index(request):
#     return HttpResponse(request, "work05_1/index.html")

# Create your views here.
from django.shortcuts import render
import datetime


def index(request):
    result = None

    if request.method == "POST":
        num1 = float(request.POST.get("num1"))
        num2 = float(request.POST.get("num2"))
        operator = request.POST.get("operator")

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2 if num2 != 0 else "エラー（0で割れません）"
    context = {"result": result}
    return render(request, "work06/index.html", context)


def reiwa_year(request):
    year: int = datetime.datetime.strptime('2019年5月1日', '%Y年%m月%d日')
    reiwa = year - 2018
    count = {"result": reiwa}
    return render(request, "work06/index.html", count)
