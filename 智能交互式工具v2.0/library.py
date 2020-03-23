import time
from passage_generator import PassageGenerator
from look_up_a import LookUp
from look_up_b import LookUp2
from translate import Translate
from _math import Math

import re
import bs4
import urllib.request  
from bs4 import BeautifulSoup 
import urllib.parse
import sys

class Conversations():
    def __init__(self):
        self.msg = input('我说: ')
        self.msg2 = self.msg
        self.msg = self.msg.replace(" ", "") # 去空格
        self.special_dictionary = {'百度百科搜索':'f1', '中英单词互译':'f2', '百度搜索引擎':'f3',
                                   '提取百度查找结果中的链接':'f3f0', '等差数列计算':'f4','几何形体计算':'f5', '完全平方数查找':'f6', '文章生成器':'f7'}

    def replace(self):
        """内容替换"""
        if "你好" in self.msg:
            self.msg = self.msg.replace("你好", "你也好")
        else:
            # 人称转换
            self.msg = list(self.msg)
            n = 0
            for i in self.msg:
                if "我" in self.msg[n]:
                    self.msg[n] = "你"
                elif "你" in self.msg[n]:
                    self.msg[n] = "我"
                n += 1
                
        self.msg = [str(j) for j in self.msg]
        self.msg = ''.join(self.msg)

        # 常规替换
        self.msg = self.msg.replace("吗", "")
        self.msg = self.msg.replace("吧", "")
        self.msg = self.msg.replace("呢", "")
        self.msg = self.msg.replace("啊", "")
        self.msg = self.msg.replace("哈", "")
        self.msg = self.msg.replace("？", "！")
        self.msg = self.msg.replace("这么", "的确")
        self.msg = self.msg.replace("那么", "的确")
        self.msg = self.msg.replace("怎么", "就那么")
        self.msg = self.msg.replace("原来", "的确")
        self.msg = self.msg.replace("真的假的", "真的")

    def special(self):
        """特殊情况"""
        if "我" in self.msg:
            if "是谁" in self.msg:
                self.msg = "我是智慧的人工智能！"
        else:
            if "谁" in self.msg:
                self.msg = "我不知道是谁呢。"
        if "哪" in self.msg:
            self.msg = "我也不清楚呢。"
            
        if "是什么" in self.msg2 or "什么是" in self.msg2:
            try:
                self.msg2 = self.msg2.replace("！", "")
                self.msg2 = self.msg2.replace("？", "")
                self.msg2 = self.msg2.replace("。", "")
                if "是什么" in self.msg2:
                    search_item = self.msg2.replace("是什么", "")
                if "什么是" in self.msg2:
                    search_item = self.msg2.replace("什么是", "")
                print("AI说: 正在为您搜索百度百科...")
                try:
                    url = 'https://baike.baidu.com/item/' + urllib.parse.quote(search_item)
                    html = urllib.request.urlopen(url)
                    content = html.read().decode('utf-8')
                    html.close()
                    soup = BeautifulSoup(content, "lxml")
                    text = soup.find('div', class_="lemma-summary").children
                    for x in text:
                        word = re.sub(re.compile(r"<(.+?)>"), '', str(x))
                        words = re.sub(re.compile(r"\[(.+?)\]"), '', word)
                        print(words)
                    if "是什么" in self.msg2:
                        self.msg = "已显示" + '"' + self.msg2.replace("是什么", "") + '"' + "的搜索结果"
                    if "什么是" in self.msg2:
                        self.msg = "已显示" + '"' + self.msg2.replace("什么是", "") + '"' + "的搜索结果"
                except AttributeError:
                    print("AI说: 没有找到相关内容")
                    self.msg = "请尝试换一种问法呢"
            except:
                print('<请检查网络>\n')

    def completion(self):
        """末尾标点补全"""
        if ("！" not in self.msg) and ("。" not in self.msg):
            self.msg = self.msg + "。"

    def _print(self):
        print("AI说:", self.msg)



class SpecialFunctions():
    def help(self,a):
        print('[查询功能命令]\n(在对话框输入相应命令即可启动功能)\n')
        print('<<<功能列表>>>')
        for dict_key, dict_value in a.special_dictionary.items():  
            print(dict_key,'->',dict_value)
        print('<<<功能列表>>>\n')

    def f1(self):
        print("[百度百科搜索](需要联网)")
        d = LookUp()
        print("")

    def f2(self):
        print("[中英单词互译](可译短语)(需要联网)")
        d = Translate()
        print("")

    def f3(self):
        print("[百度引擎查找](需要联网)\n")
        f = LookUp2()
        print("")

    def f3f0(self):
        print('[链接提取]\n')
        try:
            with open ('百度搜索结果.txt', 'r', encoding='UTF-8') as f:
                str = f.read()
                result = re.findall("'title': '([^\s]*)', 'sub_url': '([^\s]*)'", str)
                for tur in result:
                    for i in tur:
                        i = i.replace("'", "")
                        print(i, "\n")
                    print("\n")

                with open ('链接提取结果.txt', 'w', encoding='UTF-8') as f_obj:
                    for tur in result:
                        for i in tur:
                            i = i.replace("'", "")
                            f_obj.write(i + "\n")
                        f_obj.write("\n\n")
            print('提取结果已保存至"链接提取结果.txt"\n')
        except:
            print("<提取失败>\n可能是没有提取目标所导致\n")

    def f4(self):
        try:
            print("[等差数列计算]")
            a2 = int(input("首项:"))
            b2 = int(input("尾项:"))
            c2 = int(input("项差:"))
            result = (a2 + b2) * ((b2 - a2) / c2 + 1) / 2
            print("结果为:", result, "\n")
        except:
            print("<无效的输入>\n")

    def f5(self):
        print("[几何形体计算]\n")
        e = Math()
        print("")

    def f6(self):
        print("[完全平方数查找]该功能可用于查找哪一个完全平方数中含有指定的数字\n")
        try:
            number = int(input('想要查找的数字:'))
            a1 = int(input('起始位置:'))
            b1 = int(input('终止位置:'))
            c1 = int(input('步长:'))
            for i in range(a1, b1 + 1, c1):
                print("checking: " + str(i) + " ** 2 = " + str(i ** 2))
                if str(number) in str(i ** 2):
                    print("result: " + str(i) + "的平方" + "(" + str(i ** 2) + ")"
                            + "含有" + str(number) + ".\n")
                    try:
                        with open('完全平方数查找结果.txt', 'a') as file_object:
                            file_object.write("result: " + str(i) + "的平方" + "(" + str(i ** 2) + ")"
                                                + "含有" + str(number) + ".\n")
                    except:
                        with open('完全平方数查找结果', 'w') as file_object:
                            file_object.write("result: " + str(i) + "的平方" + "(" + str(i ** 2) + ")"
                                                + "含有" + str(number) + ".\n")
                    print('查找结果已保存至"平方查找结果.txt"\n')
                    break
        except:
            print("<无效的输入>\n")
            
    def f7(self):
        print("[文章生成器]该功能可用于生成狗屁不通文章\n")
        c = PassageGenerator()

    def _time(self):
        st = time.localtime()
        print("[系统时间]", st[0], "年", st[1], "月", st[2], "日",
              st[3], "时", st[4], "分", st[5], "秒", "(星期", st[6], ")")            
