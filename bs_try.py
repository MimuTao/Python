import requests
import re
from bs4 import BeautifulSoup
import csv

def GetHtml(url):
    response=requests.get(url)
    print(response.status_code)
    print(response.encoding)
    return response.text

def GetImage(html):
    soup=BeautifulSoup(html,'html.parser')
    result=soup.find_all(class_='item')
    index=100
    for item in result:
        # print(item)
        # print(str(item))

        print('--------------------------------------------------------------------------\n\n\n')
        namesoup=BeautifulSoup(str(item),'html.parser')
        stitle=namesoup.find_all('span',class_='title')
        for i in stitle:
            print(str(i.string))
        t=stitle.
        otitle=namesoup.find_all('span',class_='other')
        # img_scarch=re.search('https://.*jpg',str(item))
        # img_url=img_scarch.group()
        # print(img_url)
        # img_response=requests.get(img_url)
        # print(img_response.status_code)
        # with open('./img/'+str(index)+'.jpg','wb') as img:
        #     img.write(img_response.content)
        # index=index+1

        # print(img_url)
        # if result:
        #     print(result)
    # index=0
    # # print(result)
    # for source in result:
    #     img_url=source.get('src')
    #     if re.match('^http://.*.jpg$',img_url):
    #         print(img_url)
    #     # ret=requests.get('http:'+img_url)
    #         ret=requests.get(img_url)
    #         with open('img/'+str(index)+'.jpg','wb') as img:
    #             img.write(ret.content)
    #             index=index+1
    
ihtml=GetHtml('https://movie.douban.com/top250?start=100&filter=',)
# with open('iindex.html','wt') as page:
    # page.write(ihtml)
# print(ihtml)
GetImage(ihtml)