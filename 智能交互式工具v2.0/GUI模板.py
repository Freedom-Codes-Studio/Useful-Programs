import tkinter as tk

window = tk.Tk()
window.title('智能交互式工具')
window.geometry('1300x700')
 
 
标签 = tk.Label(window, text='<<<智能交互式工具>>>  VERSION:v2.0  AUTHOR:Du_Yun', font=("黑体",20), width=1300, height=4)
标签.pack()

帮助 = tk.Button(window, text="帮助", font=("黑体","15"), width=30, height=3)
帮助.pack()
帮助.place(x=950,y=100)

关于 = tk.Button(window, text="关于", font=("黑体","15"), width=30, height=3)
关于.pack()
关于.place(x=950,y=180)

退出 = tk.Button(window, text="退出", font=("黑体","15"), width=30, height=3)
退出.pack()
退出.place(x=950,y=260)

百度百科搜索 = tk.Button(window, text="百度百科搜索", font=("黑体","15"), width=15, height=3)
百度百科搜索.pack()
百度百科搜索.place(x=30,y=100)

中英单词互译 = tk.Button(window, text="中英单词互译", font=("黑体","15"), width=15, height=3)
中英单词互译.pack()
中英单词互译.place(x=195,y=100)

百度搜索引擎 = tk.Button(window, text="百度搜索引擎", font=("黑体","15"), width=15, height=3)
百度搜索引擎.pack()
百度搜索引擎.place(x=360,y=100)

提取搜索链接 = tk.Button(window, text="提取搜索链接", font=("黑体","15"), width=15, height=3)
提取搜索链接.pack()
提取搜索链接.place(x=525,y=100)

等差数列计算 = tk.Button(window, text="等差数列计算", font=("黑体","15"), width=15, height=3)
等差数列计算.pack()
等差数列计算.place(x=690,y=100)

几何形体计算 = tk.Button(window, text="几何形体计算", font=("黑体","15"), width=15, height=3)
几何形体计算.pack()
几何形体计算.place(x=30,y=180)

完全平方数查找 = tk.Button(window, text="完全平方数查找", font=("黑体","15"), width=15, height=3)
完全平方数查找.pack()
完全平方数查找.place(x=195,y=180)

文章生成器 = tk.Button(window, text="文章生成器", font=("黑体","15"), width=15, height=3)
文章生成器.pack()
文章生成器.place(x=360,y=180)

更多功能敬请期待 = tk.Button(window, text="更多功能敬请期待", font=("黑体","15"), width=31, height=3)
更多功能敬请期待.pack()
更多功能敬请期待.place(x=530,y=180)

我说 = tk.Label(window, text="我说:", font=("黑体","25"))
我说.pack()
我说.place(x=30, y=270)

输入栏 = tk.Text(window, font=("黑体","15"), width=60, height=2)
输入栏.pack()
输入栏.place(x=150, y=270)

发送 = tk.Button(window, text="发送", font=("黑体","20"), width=5, height=1)
发送.pack()
发送.place(x=760, y=270)

信息栏 = tk.Text(window, font=("黑体","15"), width=85, height=17)
信息栏.pack()
信息栏.place(y=350)

状态栏 = tk.Label(window, text="本程序仅供学习交流，不得用于商业用途；", font=("黑体","15"))
状态栏.pack
状态栏.place(x=900, y = 350)

状态栏2 = tk.Label(window, text="不当使用本程序带来的后果需自行承担。", font=("黑体","15"))
状态栏2.pack
状态栏2.place(x=900, y = 380)
 
window.mainloop()