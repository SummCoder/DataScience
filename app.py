from flask import Flask, render_template, request
from climb import main
from translate import translate
from eda import inputEDA
from store import save_db
import sqlite3

app = Flask(__name__)


@app.route('/')  # 首页
def index():  # put application's code here
    return render_template("index.html")


@app.route('/climb')  # 爬取操作
def climb():  # put application's code here
    main()
    return render_template("index.html")


@app.route('/trans')  # 回译
def trans():  # put application's code here
    datalist = []
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    sql = "select * from store"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    new_data = datalist[len(datalist) - 1]
    cur.close()
    con.close()
    return render_template("trans1.html", real_date=new_data)


@app.route('/eda')  # EDA
def eda():  # put application's code here
    datalist = []
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    sql = "select * from store"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    new_data = datalist[len(datalist) - 1]
    cur.close()
    con.close()
    return render_template("eda.html", real_date=new_data)


@app.route('/amp')  # 嵌入操作
def amp():  # put application's code here
    datalist = []
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    sql = "select * from store"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    new_data = datalist[len(datalist) - 1]
    cur.close()
    con.close()
    return render_template("amp.html", real_date=new_data)


@app.route('/com')  # 比较
def com():  # put application's code here
    datalist = []
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    sql = "select * from store"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    new_data = datalist[len(datalist) - 1]
    cur.close()
    con.close()
    return render_template("com.html", real_date=new_data)


@app.route('/function', methods=["GET", "POST"])
def function():
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        text = request.files.get('che')
        if keyword != '':
            data1, data2, data3, BleuScore, BleuScore1 = translate(keyword)
            data4, BleuScore2 = inputEDA(keyword)
            save_db(data1, data2, data3, BleuScore, BleuScore1, data4, BleuScore2)
            # return render_template('index.html')
        if text.filename != '':
            text.save(text.filename)
            f = open(text.filename, mode="r", encoding="utf-8")   # 第一个参数为 文件路径：分为相对路径和绝对路径，这里为相对路径;第二个为对文件袋的操作方式，第三个为编码
            content = f.read()
            f.close()
            data1, data2, data3, BleuScore, BleuScore1 = translate(content)
            data4, BleuScore2 = inputEDA(content)
            save_db(data1, data2, data3, BleuScore, BleuScore1, data4, BleuScore2)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
