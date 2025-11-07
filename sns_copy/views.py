from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "sns_copy/home.html")


def notice(request):
    return render(request, "sns_copy/notice.html")


def search(request):
    return render(request, "sns_copy/search.html")


def profile(request):
    return render(request, "sns_copy/profile.html")


def posting(request):
    return render(request, "sns_copy/posting.html")
