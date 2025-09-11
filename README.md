# python-apps-django
## サーバーの起動

'python manage.py runserver'

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('work05.urls')),
    path('work05_1/', include('work05_1.urls')),
]

##　新しくアプリを作るコード
"python manage.py startapp 自分が作りたい物の名前"

## 手順
"手順
１.親フォルダー
　　　｜ー　自分が作りたい物の名前
　　　　　　　　　　｜ーtemplates/　←これを作る
                        |-index.html ←これを作る
　　　｜ーpython_apps_django
２.portfolioにurl.pyのファイルを作る
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
]
をコピペする
３.# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
     return render(request, "自分がつくりたい物の名前/index.html")
def index(request):
     return HttpResponse(request, "自分が作りたい物の名前/index.html")

Create your views here.
をコピぺする
４.python_apps_djangoのurls.pyに
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('work05.urls')),
    path('work06/', include('work06.urls')),
    path('自分が作りたい物の名前/', include('自分が作りたい物の名前.urls')), ←これを追加する
]
５,python_apps_djangoのsettings.pyに
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'work05',
    'work06',
    'portfolio',←自分の作りたい物の名前を追加
]



"