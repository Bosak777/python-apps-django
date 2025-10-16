# from django.http import HttpResponse
# from django.shortcuts import render


# def index(request):
#     return render(request, "work05_1/index.html")
# def index(request):
#     return HttpResponse(request, "work05_1/index.html")

# Create your views here.
from django.shortcuts import render
import random


def omikuji(request):
    unda = None
    if request.method == "POST":
        choices = ['大吉', '中吉', '小吉', '吉', '末吉', '凶', '大凶',]
        unda = random.choice(choices)

    return render(request, "work07/index.html", {"result": unda})
