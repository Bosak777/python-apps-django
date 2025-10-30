from django.shortcuts import render, redirect
from .models import Memo  # モデル名に合わせてください
import mysql.connector
from datetime import datetime


def index(request):
    filter_option = request.GET.get('filter', 'all')

    if filter_option == 'completed':
        memos = Memo.objects.filter(is_done=True)
    elif filter_option == 'uncompleted':
        memos = Memo.objects.filter(is_done=False)
    else:
        memos = Memo.objects.all()

    return render(request, 'work09/index_todo.html', {
        'memos': memos, 'filter_option': filter_option
        })


def todo_task(request):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='bosaklong',
        database='work09'
    )
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST':
        title = request.POST.get('title')  # タスク名
        deadline = request.POST.get('deadline')  # 期限
        entyr_time = datetime.now()  # 登録日時

        if title and deadline:
            cursor.execute(
                'insert into todo (task_name, deadline, entry) values('
                '%s, %s, %s)',
                (title, deadline, entyr_time)
            )
            conn.commit()
            cursor.close()
            conn.close()
            return redirect('index_todo')  # url名がindex_todoならここもOK
    cursor.execute('select * from todo order by entry desc')
    todo_list = cursor.fetchall()
    cursor.close()
    conn.close()

    return render(request, 'work09/todo_list.html', {'tasks': todo_list})
#  データベース; work09
#  テーブル: todo
#  カラム: task_name,deadline,entry
