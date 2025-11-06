# from django.http import HttpResponse
# from django.shortcuts import render


# def index(request):
#     return render(request, "work05_1/index.html")
# def index(request):
#     return HttpResponse(request, "work05_1/index.html")

# Create your views here.
import mysql.connector
from django.shortcuts import render
import os

# from .models import Memo


def memo(request):
    conn = mysql.connector.connect(
        host=os.environ.get("DB_HOST", "mysql.railway.internal"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASSWORD", ""),
        database=os.environ.get("DB_NAME", "railway"),
        port=os.environ.get("DB_PORT", 3306),
    )
    cursor = conn.cursor(dictionary=True)

    # メモタイトルを取得
    cursor.execute("SELECT id, title FROM work08_memo ORDER BY id DESC")
    memos = cursor.fetchall()

    cursor.close()
    conn.close()

    # index_top.html にデータを渡す
    return render(request, "work08/index_top.html", {"memos": memos})


def add_memo(request):
    result = None
    if request.method == "POST":
        print("受信しました")
        title = request.POST.get("title")
        content = request.POST.get("content")

        conn = mysql.connector.connect(
            host="localhost", user="root", password="bosaklong",
            database="work08"
        )
        # カーソル作成
        cursor = conn.cursor()
        # データを挿入
        query = "insert into memo (title, content) values (%s, %s)"
        cursor.execute(query, (title, content))
        conn.commit()
        cursor.close()
        conn.close()
        result = "保存しました"
    return render(request, "work08/add_memo.html", {"result": result})


#  データベース;work08
#  テーブル:memo
#  カラム:id, title, content
