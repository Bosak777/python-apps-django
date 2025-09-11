# from django.http import HttpResponse
# from django.shortcuts import render


# def index(request):
#     return render(request, "work05_1/index.html")
# def index(request):
#     return HttpResponse(request, "work05_1/index.html")

# Create your views here.
from django.shortcuts import render


def index(request):
    result = None
    if request.method == "POST":
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        operator = request.POST.get("operator")

        if num1 and num2:  # どちらも空じゃないときだけ計算
            num1 = float(num1)
            num2 = float(num2)

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "エラー: 0で割れません"

    return render(request, "work06/index.html", {"result": result})


def reiwa_year(request):
    kei = None
    if request.method == "POST":
        year = request.POST.get("year")  # 1回だけでOK
        if year:  # 値が入っていれば処理
            year = int(year)
            kei = year + 2018
    return render(request, "work06/index.html", {"kei": kei})
