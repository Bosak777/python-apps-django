from django.shortcuts import render


def index(request):
    # templates/top_page/index.html を返す
    return render(request, 'top_page/index.html')
