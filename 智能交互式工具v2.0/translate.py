# -*- coding: utf-8 -*-
 
"""
功能：百度翻译
注意事项：中英文自动切换
"""
 
import requests
import re
 
 
class Baidu_Translate(object):
    def __init__(self, query_string):
        self.query_string = query_string
        self.url_1 = 'https://fanyi.baidu.com/sug'
        # self.url = 'https://fanyi.baidu.com/v2transapi'  # 这里不能用这个地址，因为对方采用了反爬虫措施，访问这个地址是人家是不会给你任何数据的
        self.url_0 = 'https://fanyi.baidu.com/transapi'
        self.zh_pattern = re.compile('[\u4e00-\u9fa5]+')
        self.headers = {
            'Accept': '* / *',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh-CN, zh; q=0.9',
            'Connection': 'keep - alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
 
    def get_post_data(self):
        """
        拿到 post 请求上传的参数，并判断输入类型并予以返回
        :return: 查询词
        """
        if re.search(pattern=self.zh_pattern, string=self.query_string):  # 输入的内容含有中文，则判别其为中文输入
            return {
            "from": "zh",
            "to": "en",
            "kw": self.query_string,  # 模糊查询 url_1关键词
            "query": self.query_string,  # 精准查询 url_0关键词
        }
        else:
            return {
            "from": "en",
            "to": "zh",
            "kw": self.query_string,  # 模糊查询 url_1关键词
            "query": self.query_string,  # 精准查询 url_0关键词
            }
 
    def request_translate(self):
        """
        向百度请求 json 数据
        :return: 向百度请求的 json 数据
        """
        data = self.get_post_data()
        try:
            response_0 = requests.request(method="post", url=self.url_0, headers=self.headers, data=data).json()
        except Exception:  # 进行数据请求的任何异常处理
            response_0 = ''
        try:
            response_1 = requests.request(method="post", url=self.url_1, headers=self.headers, data=data).json()
        except Exception:  # 进行数据请求的任何异常处理
            response_1 = ''
        return response_0, response_1
 
    def parse_translate_data(self):
        """
        数据解析，将请求到的翻译内容解析并输出
        :return: None
        """
        response_0 = self.request_translate()[0]
        response_1 = self.request_translate()[1]
        # item = response_0
        if response_0:
            item = response_0.get('data')[0].get('dst')
            print('key word:', self.query_string, '\t', 'translate:', item)
        if response_1:
            data = response_1.get('data')
            print()
            for item in data[:1]:  # 长度一般为5，这里只保留其释义
                print('key word: \t[ {key} ]'.format(key=item.get('k')))
                print('value: \t\t[ {value} ]'.format(value=item.get('v')))
                print()
        # print(response_1.get('data'))
 
 
def main():
    """
    主函数
    :return: None
    """
    while True:
        try:
            query_keywords = input("""想要翻译的内容 [ 输入"/out"退出 ]:""")
            if query_keywords == "/out":  # 如果输入/out，退出小程序
                break
            else:
                baidu = Baidu_Translate(query_string=query_keywords)
                baidu.parse_translate_data()
        except Exception as e:
            print('请求出错，请重试', e.args)

class Translate():
     def __init__(self):
         main()
