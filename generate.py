#!usr/bin/python3
#coding=utf-8

from databaseConnect import insert,delete,select
#import sqlite3
#from dataProcess import process

def output_html(word):
    insert(word) #创建、插入数据库由word组成的表
    datas = select(word)
    fout = open('output.html','w')
    
    fout.write("""    
    <html>
    <head> 
    <meta charset="utf-8"> 
    <title>任意字符查询及比对</title> 
    <style>
    #logo{
        position:relative;
        left:200px;
        width:1000px;
        height:154px;
        border:0px solid black;
        text-align: center;
    }
    </style>
    </head>
    <body>
    <div id="logo">
    <img border="0" src="use.jpg"alt="" width="1000" height="100">
    </div>
    <table width="100%" border="1" cellspacing="0" cellpadding="0" align="center">
    <tr>
        <th>标题</th>
        <th>摘要</th>
        <th>词频</th>
        <th>词频比(%)</th>
        <th>排名(最初)</th>
        <th>排名(最新)</th>
        <th>登记时间</th>
        <th>链接</th>
    </tr>
    """)
    
    for data in datas:
        fout.write("<tr>")
        fout.write("<td width='20%%'> %s</td>" % data["title"])
        fout.write("<td width='30%%'> %s</td>" % data["summary"])
        fout.write("<td width='5%%'> %s</td>" % data["times"])
        fout.write("<td width='5%%'>%s</td>" % data["fre"]) #.encode("utf-8")
        fout.write("<td width='5%%'> %s</td>" % data["preRank"])
        fout.write("<td width='5%%'>%s</td>" % data["newRank"])
        fout.write("<td width='10%%'> %s</td>" % data["time"])
        format = """<td width='10%%'> <a href="%s" target="_blank"> %s </a> </td>"""
        values = (data["link"], data["link"])
        fout.write(format % values)
        fout.write("</tr>")
    
    fout.write("</table>")
    fout.write("</body>")
    fout.write("</html>")
    fout.close()

if __name__=='__main__':
    word = raw_input("Enter items you want to search: ")
    output_html(word)
    flag = raw_input("IF delete table from database:(Y for yes,else for no): ")
    if flag == 'y' or flag == 'Y':
        delete(word) #删除由word组成的表
    else:
        print("System end")
    