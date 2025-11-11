from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "sns/home.html")


def notice(request):
    return render(request, "sns/notice.html")


def search(request):
    return render(request, "sns/search.html")


def profile(request):
    return render(request, "sns/profile.html")


def posting(request):
    return render(request, "sns/posting.html")
