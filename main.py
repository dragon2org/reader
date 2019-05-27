# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests

"""
从www.biqubao.com笔趣阁爬取小说，楼主教程中的网址我当时没打开，
就参照楼主教程，爬取了笔趣阁小说网的内容。
    2018-07-31
"""

if __name__ == '__main__':
    target = "https://www.biquge.info/3_3746/"
    req = requests.get(url=target)
    req.encoding = 'utf-8'

    soup=BeautifulSoup(req.text, "html.parser")
    list_tag = soup.div(id="list")
    list_tag = list_tag[0].find_all('a')


