#!usr/bin/python3
#coding=utf-8
from __future__ import division
import requests, re, bs4
import urllib
import urllib2
from bs4 import BeautifulSoup as BS
from dataCollection import collection
import operator  

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def process(word):#对获取数据进行处理，主要为排序
    datas = collection(word)

    for data in datas:#计算频率及出现次数
        frequency(data, word)

    #newDatas = sorted(datas, cmp = sortList,reverse = True)
    sorted_data = sorted(datas, key = operator.itemgetter('fre'), reverse = True)#对列表中的字典进行排序
    count = 0
    for data in sorted_data:
        count = count + 1
        data["newRank"] = count
#         print(data["title"])
#         print(data["link"])
#         print(data["time"])
#         print(data["summary"])
#         print(data["preRank"])
#         print(data["times"])
#         print(data["fre"])
        
    return sorted_data

def frequency(data, word):#获取字符串词频
    try:
        request = urllib2.Request(data["link"])
        response = urllib2.urlopen(request)
    except urllib2.HTTPError, e:  #输出错误信息已注释，出错直接赋值为0
#         print e.getcode()  
#         print e.reason  
#         print e.geturl()  
#         print "-------------------------"  
#         print e.info()  
#         print e.read()  
        data["times"] = 0
        data["fre"] = 0
        return
    except urllib2.URLError as e:
        data["times"] = 0
        data["fre"] = 0
        print (e.reason)
        return
        
    html = response.read()
    soup = BS(html,'html.parser',from_encoding = "utf-8")
    
    for x in soup.find_all('script'):
        x.extract() 
    text = soup.get_text()
    text = ' '.join(re.split(' +|\n+', text)).strip()
    time = text.count(word)
    if(len(text) == 0):
        data["times"] = 0
        data["fre"] = 0
    else:
        fre = round(time / len(text) * 100,2)
        data["times"] = time
        data["fre"] = fre

def sortList(data1, data2):#对data中数据根据词频进行排序
    if data1["fre"] - data2["fre"] < 0:
        return -1
    elif data1["fre"] - data2["fre"] == 0:
        return 0
    else:
        return 1


    
