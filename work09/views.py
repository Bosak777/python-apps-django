# from django.http import HttpResponse
# from django.shortcuts import render


# def index(request):
#     return render(request, "work05_1/index.html")
# def index(request):
#     return HttpResponse(request, "work05_1/index.html")

# Create your views here.
import mysql.connector
from django.shortcuts import render
# from .models import Memo


def index_todo(request):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='bosaklong',
        database='work08'
    )
    cursor = conn.cursor(dictionary=True)

    # メモタイトルを取得
    cursor.execute("select id, title from memo order by id desc")
    memos = cursor.fetchall()

    print(memos)

    cursor.close()
    conn.close()
    # index_top.hmtlにデータを渡す
    return render(request, 'work09/index_todo.html', {"memos": memos})


def todo_list(request):
    result = None
    if request.method == "POST":
        print("受信しました")
        title = request.POST.get("title")
        content = request.POST.get("content")

        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='bosaklong',
            database='work08'
        )
        # カーソル作成
        cursor = conn.cursor()
        # データを挿入
        query = 'insert into memo (title, content) values (%s, %s)'
        cursor.execute(query, (title, content))
        conn.commit()
        cursor.close()
        conn.close()
        result = "保存しました"
    return render(request, "work09/todo_list.html", {'result': result})

#  データベース;
#  テーブル:
#  カラム:id,
