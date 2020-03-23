"""
Created on Fri Aug 18 15:58:13 2017
@author: JClian
"""
import re
import bs4
import urllib.request  
from bs4 import BeautifulSoup 
import urllib.parse
import sys

class LookUp():
    def __init__(self):
        try:
            search_item = input('想要搜索的内容(输入"/out"以退出):')
            while search_item != '/out':
                if search_item == '/out':
                    exit(0)
                print("正在搜索...")
                try:
                    url = 'https://baike.baidu.com/item/' + urllib.parse.quote(search_item)
                    html = urllib.request.urlopen(url)
                    content = html.read().decode('utf-8')
                    html.close()
                    soup = BeautifulSoup(content, "lxml")
                    text = soup.find('div', class_="lemma-summary").children
                    print("搜索结果:")
                    for x in text:
                        word = re.sub(re.compile(r"<(.+?)>"), '', str(x))
                        words = re.sub(re.compile(r"\[(.+?)\]"), '', word)
                        print(words)
                except AttributeError:
                    print("没有找到相关内容")
                search_item = input('想要搜索的内容(输入"/out"以退出):')
        except:
            print('<请检查网络>\n')
