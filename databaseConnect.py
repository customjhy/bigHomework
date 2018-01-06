#!usr/bin/python3
#coding=utf-8

import sqlite3
from dataProcess import process

def initial():
    conn = sqlite3.connect('search.db')
    print("Opened database successfully")

def insert(word):
    datas = process(word)
    
    #连接数据库
    conn = sqlite3.connect('search.db')
    print("Opened database successfully,Create begin")
    #创建表格
    c = conn.cursor()
    format = '''CREATE TABLE IF NOT EXISTS %s
            (TITLE TEXT PRIMARY KEY NOT NULL,
            LINK           TEXT    NOT NULL,
            TIME           TEXT     NOT NULL,
            SUMMARY        TEXT     NOT NULL,
            PRERANK        INT     NOT NULL,
            TIMES          INT     NOT NULL,
            FRE            FLOAT     NOT NULL,
            NEWRANK        INT     NOT NULL);''' 
    values = (word)
    c.execute(format % values)

    print("Table created successfully,Insert begin")
    conn.commit()
    #插入数据
    for data in datas:
        format = "REPLACE  INTO %s (TITLE,LINK,TIME,SUMMARY,PRERANK,TIMES,FRE,NEWRANK) \
                VALUES ('%s', '%s', '%s', '%s', %d, %d, %f, %d)"
        values = (word, data["title"], data["link"], data["time"], 
                data["summary"], data["preRank"], data["times"], data["fre"], data["newRank"])
        c.execute(format % values)
    conn.commit()
    print("Records created successfully")
    conn.close()

def delete(word):#删除所创建的表
    conn = sqlite3.connect('search.db')
    c = conn.cursor()
    print("Opened database successfully,Delete begin")

    c.execute("DROP TABLE %s" % word)
    conn.commit()
    print("Delete completed")

def select(word):
    conn = sqlite3.connect('search.db')
    c = conn.cursor()
    print("Opened database successfully")
    
    cursor = c.execute("SELECT TITLE,LINK,TIME,SUMMARY,PRERANK,TIMES,FRE,NEWRANK from %s" % word)
    datas = []
    for row in cursor:
        data = {}
        data["title"] = row[0]
        data["link"] = row[1]
        data["time"] = row[2]
        data["summary"] = row[3]
        data["preRank"] = row[4]
        data["times"] = row[5]
        data["fre"] = row[6]
        data["newRank"] = row[7]
        datas.append(data)
    print("Select operation done successfully")
    conn.close()
    return datas


