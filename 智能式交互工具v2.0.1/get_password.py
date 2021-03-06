import random

class GetPassword():
    def __init__(self):
        字母词典 = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',
                         7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',
                         13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',
                         19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',
                         25:'y',26:'z'}
        符号词典 = {1:"~", 2:"!", 3:"@", 4:"#", 5:"$", 6:"%", 7:"^", 8:"&", 9:"*",
                       10:"(", 11:")", 12:"{", 13:"}", 14:"[", 15:"]", 16:"|", 17:":", 
                       18:";", 19:"'", 20:"<", 21:">", 22:",", 23:".", 24:"?", 25:"/",
                        26:"-", 27:"_", 28:"+", 29:"="}
                    
        def 一般生成(位数, 复杂等级):
            生成结果 = ""
            while len(生成结果) < 位数:
                if 复杂等级 == 1:
                    生成结果 += str(random.randint(0,9))
                elif 复杂等级 == 2:
                    判断 = random.randint(1,2)
                    if 判断 == 1:
                        生成结果 += 字母词典[random.randint(1,26)]
                    elif 判断 == 2:
                        生成结果 += str(random.randint(0,9))
                elif 复杂等级 == 3:
                    判断 = random.randint(1,3)
                    if 判断 == 1:
                        生成结果 += 字母词典[random.randint(1,26)]
                    elif 判断 == 2:
                        生成结果 += 字母词典[random.randint(1,26)].upper()
                    elif 判断 == 3:
                        生成结果 += str(random.randint(0,9))
                elif 复杂等级 == 4:
                    判断 = random.randint(1,4)
                    if 判断 == 1:
                        生成结果 += 字母词典[random.randint(1,26)]
                    elif 判断 == 2:
                        生成结果 += 字母词典[random.randint(1,26)].upper()
                    elif 判断 == 3:
                        生成结果 += str(random.randint(0,9))
                    elif 判断 == 4:
                    	生成结果 += 符号词典[random.randint(1, 29)]
            print("生成结果为:", 生成结果)
            with open("密码生成结果.txt", "a") as 保存:
                保存.write(生成结果)
            print('生成结果已保存至"密码生成结果.txt"\n')

        try:
            位数 = int(input("请输入密码的位数:"))
            复杂等级 = int(input("复杂等级(1为纯数字，2为数字加小写字母，\n3为数字加大小写字母，4为数字、大小写字母与常规符号的混合):"))
            一般生成(位数, 复杂等级)
        except:
            print("<无效的输入>\n")
