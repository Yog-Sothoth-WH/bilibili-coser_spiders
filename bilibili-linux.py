
import requests
import re
from urllib.parse import urlencode
import os
import sys
import time
import json

def getnewpg_new (page_num):
    #构成ajax
    page_num = str(page_num)
    head_url = 'https://api.vc.bilibili.com/link_draw/v2/Photo/list?'
    data = {'category': 'cos' , 'type' : 'new' ,'page_num':page_num ,'page_size':'20'}
    URL = head_url + urlencode (data)
    return URL

def getinfo (URL):
    #访问返回段落
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
    req = requests.get(URL,headers = head)
    return req.text

def getdownloadurl (result):
    #分割段落
    result = result.replace(' ','')
    result = re.sub('category',' ',result)
    p = re.compile('"pictures":'+'\S*')
    part = re.findall(p,result)
    for i in part:
        #提取标题避免非法字符，创建文件夹
        p_title = re.compile('"title":"'+'\S*')
        title = re.findall(p_title,i)
        title = str(title)
        title = title.replace('[\'"title":"','')
        title = title.replace('","\']','')
        title = title.replace('\\','')
        title = title.replace('/','')
        title = title.replace(':','')
        title = title.replace('*','')
        title = title.replace('?','')
        title = title.replace('"','')
        title = title.replace('>','')
        title = title.replace('<','')
        title = title.replace('|','')
        print (title)
        try:
            os.mkdir(title)
        except:
            while(1):
                try:
                    namee = str(uim)
                    title = title+namee
                    os.mkdir(title)
                    break
                except :
                    uim + 1
                    continue
        p_url = re.compile('https://'+'\w*'+'\.'+'\w*'+'\.'+'\w*'+'\/bfs\/album\/'+'\w*'+'.jpg')
        urlpage = re.findall(p_url,i)
        for d in urlpage:
            print(d)
            head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
            dwld = requests.get(d,headers = head)
            dwld = dwld.content
            image_name = re.findall('\w{12,}'+'.jpg',d)
            image_name = str(image_name)
            image_name = image_name.replace('[\'','')
            image_name = image_name.replace('\']','')
            fileadrees = title +'/'
            with open (fileadrees+image_name,'wb') as f:
                f.write(dwld)
            time.sleep(0.25)
        print('已完成！')
        
global uim   
uim = 1
num = 0
while (1):
    try:
        URL = getnewpg_new(num)
        result = getinfo(URL)
        getdownloadurl(result)
        num = num + 1
    except:
        break

print('程序结束！')
sys.exit()