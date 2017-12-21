import requests
from bs4 import BeautifulSoup
import re
import csv

header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

url_list = ['https://movie.douban.com/top250?start=%d' % index for index in range(0, 250, 25)]

# url = 'https://movie.douban.com/top250?start=0'


def movie_list(url):
    response = requests.get(url, header)
    response.encoding = 'utf-8'
    html = BeautifulSoup(response.text, 'html.parser')
    data = html.find('ol', {'class': 'grid_view'})
    m_list = data.find_all('li')
    movies = []
    for m in m_list:
        # rank = m.find('em').get_text()  # 排名
        rank = m.find('em').text  # 排名
        m_name = m.find('img')['alt']  # 获取电影名字
        info = m.find('p').get_text()
        director = re.findall('导演:\s(.*?)\s', info)[0]  # 导演
        starring = re.findall('主演:\s(.*?)\s', info) # 主演
        if len(starring) == 0:
            starring = '佚名'  # 因为豆瓣显示不全，所以。。
        else:
            starring = starring[0]
        year = re.search(r'\d{4}', info).group()  # 获取年份
        area_list = re.findall('\s/\s(.*?)\s/\s', info)
        # area = re.search(r'\/\n{*}\n\/', info)
        if len(area_list) > 1:
            area = area_list[1]
        else:
            area = area_list[0]
        grade = m.select('span.rating_num')[0].get_text() # 评分
        quote_l = m.select('span.inq') # 简介？
        if len(quote_l) == 0:
            quote = ''
        else:
            quote = quote_l[0].get_text()

        tup = (rank, m_name, director, starring, year, area, grade, quote)
        movies.append(tup)
    return movies

# 将内容保存到csv文件肿
# def save_data():
#     headers = ['排名', '名字', '导演', '主演', '年份', '地区', '评分', '简介']
#     with open('/Users/mocokoo/Documents/py_file/douban_movie_top250.csv', encoding='UTF-8', mode='w') as f:
#         f_csv = csv.writer(f)
#         f_csv.writerow(headers)
#         for url in url_list:
#             data_list = movie_list(url)
#             for data in data_list:
#                 f_csv.writerow(data)
ilist=[]
for url in url_list:
    data_list = movie_list(url)
    for data in data_list:
        ilist.append(data)

print(ilist)