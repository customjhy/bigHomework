#!usr/bin/python3
#coding=utf-8

import urllib
import urllib2
import re
from bs4 import BeautifulSoup as BS
#from urllib import error

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def collection(word):#word为搜索关键词
    baseUrl = 'http://www.baidu.com/s'
    count = 0;#计数,达到20就break
    datas = []

    for page in [1,2,3]:#第几页
        data = {'wd':word,'pn':str(page-1)+'0','tn':'baidurt','ie':'utf-8','bsst':'1'}
        data = urllib.urlencode(data)
        url = baseUrl+'?'+data
        #数据获取，加入错误处理
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
        except error.HTTPError as e:
            print (e.code)
            exit(0)
        except error.URLError as e:
            print (e.reason)
            exit(0)


        html = response.read()
        soup = BS(html,'html.parser',from_encoding = "utf-8")
        td = soup.find_all(class_='f')

        for t in td:
            data = {}
            data["title"] = t.h3.a.get_text().strip()  #标题
            data["link"] = t.h3.a['href'] #链接
            
            #对数据进行处理，font分解为time和summary
            font_str = t.find_all('font',attrs={'size':'-1'})[0].get_text()
            start = 0 #起始
            end = font_str.find('...')
            summ = ' '.join(re.split(' +|\n+', font_str[start:end+3])).strip()
            if summ == '':
                data["time"] = "0000-00-00"
                data["summary"] = "NULL"
            else:
                data["time"] = summ[0:10]
                data["summary"] = ' '.join(re.split(' +|\n+', summ[10:])).strip()
            #data["summary"] = font_str[start:end+3].strip()  #摘要
            count = count + 1
            data["preRank"] = count
            datas.append(data)
            if count == 15:
                return datas

    return datas        