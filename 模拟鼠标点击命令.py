import pyautogui,time,win32api,win32con,pyperclip
text=str(input("你想向剪贴板里输入什么:"))
print("本机坐标是700,960")
a=int(input("横坐标为:"))
b=int(input("纵坐标为:"))
c=int(input("你想发多少信息:"))
print("程序三秒后运行")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
print("正在运行中,按ctrl+c可强行停止")
i=0
pyautogui.click(a,b)
try:
    while i<c:
        pyperclip.copy(text+str(i))#向剪贴板里发信息
        win32api.keybd_event(162,0,0,0)#按下ctrl
        win32api.keybd_event(86,0,0,0)#按下v
        win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0)#松开v
        win32api.keybd_event(162,0,win32con.KEYEVENTF_KEYUP,0)#松开ctrl
        win32api.keybd_event(162, 0, 0, 0)  # 按下ctrl
        win32api.keybd_event(13, 0, 0, 0)  # 按下enter
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开enter
        win32api.keybd_event(162, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开ctrl
        i=i+1
        time.sleep(6)
except KeyboardInterrupt:
    print("Fuck you")
    sys.exit(0)
input("")


