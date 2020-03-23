from library import *

print(">>>欢迎使用智能交互式工具\n>>>VERSION:v2.0\n>>>支持对话语言:中文\n\n<输入/help以查询功能命令>\n")
while True:
    # 创建负责程序逻辑的类的实例
    a = Conversations()
    b = SpecialFunctions()


    # 特殊功能实现
    if a.msg == "/help":
        b.help(a)
    elif a.msg == a.special_dictionary['百度百科搜索']:
        b.f1()
    elif a.msg == a.special_dictionary['中英单词互译']:
        b.f2()
    elif a.msg == a.special_dictionary['百度搜索引擎']:
        b.f3()
    elif a.msg == a.special_dictionary['提取百度查找结果中的链接']:
        b.f3f0()
    elif a.msg == a.special_dictionary['等差数列计算']:
        b.f4()
    elif a.msg == a.special_dictionary['几何形体计算']:
        b.f5()
    elif a.msg == a.special_dictionary['完全平方数查找']:
        b.f6()
    elif a.msg == a.special_dictionary['文章生成器']:
        b.f7()
    elif a.msg == "时间":
        b._time()
        
    
    # 常规对话实现
    else:
        a.replace()
        a.special()
        a.completion()
        a._print()
