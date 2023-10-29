# 用于存储处理好的临时数据
# encoding=utf-8
import sqlite3


def save_db(data1, data2, data3, BleuScore, BleuScore1, data4, BleuScore2):
    dbpath = "store.db"
    # init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    data1 = '"' + data1 + '"'
    data2 = '"' + data2 + '"'
    data3 = '"' + data3 + '"'
    data4 = '"' + data4 + '"'
    BleuScore = str(BleuScore)
    BleuScore1 = str(BleuScore1)
    BleuScore2 = str(BleuScore2)
    da = [data1, data2, data3, BleuScore, BleuScore1, data4, BleuScore2]

    sql = '''
    insert into store(
    old_text, tran_text1, tran_text2, tran_score1, tran_score2, eda_text, eda_score1)
    values(%s)''' % ",".join(da)
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()


# def init_db():
#     dbpath = "store.db"
#     sql = '''
#     create table store
#     (
#     old_text text,
#     tran_text1 text,
#     tran_text2 text,
#     tran_score1 numeric ,
#     tran_score2 numeric ,
#     eda_text text,
#     eda_score1 numeric
#     )
#     '''
#     conn = sqlite3.connect(dbpath)
#     cursor = conn.cursor()
#     cursor.execute(sql)
#     conn.commit()
#     conn.close()


# init_db()
# def store1(data1, data2, data3, BleuScore, BleuScore1, data4, BleuScore2):
#     dbpath = "store.db"
#     save_db(data1, data2, data3, BleuScore, BleuScore1, data4, BleuScore2, dbpath)
