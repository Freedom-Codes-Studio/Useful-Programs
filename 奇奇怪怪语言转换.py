# Useful-Programs
欢迎进行添改
def encrypt(language,text):
    encrypt_text = []
    for i in text:
        encrypt_text.append(int(ord(i)))
    for j in range(len(encrypt_text)):
        encrypt_text[j] = bin(encrypt_text[j])[2:]
    for n in range(len(encrypt_text)):
        encrypt_text[n] = list(encrypt_text[n])
    a = -1
    if language == "自定义":
        c = input("输入自定义的语言(两个字)\n")
    elif language == "喵语":
        c = "喵呜"
    elif language == "叽咕语":
        c ="叽咕"
    while a <= len(encrypt_text):
        try:
            a += 1
            for m in range(len(encrypt_text[a])):
                if encrypt_text[a][m] == "0":
                    encrypt_text[a][m] = c[0]
                elif encrypt_text[a][m] == "1":
                    encrypt_text[a][m] = c[1]
        except:
            break
    for x in encrypt_text:
        print(*x,",",end="")
    return c[:2]

def decode(text):
    o = text[-2]
    t = text[-1]
    text = text[:-3].split(",")
    t2 = []
    for i in text:
        t2.append(i.split(" ")[:-1])
    n = -1
    while n <= len(t2):
        n += 1
        try:
            for j in range(len(t2[n])):
                if t2[n][j] == o:
                    t2[n][j] = '0'
                elif t2[n][j] == t:
                    t2[n][j] = "1"
        except:
            break
    for x in t2:
        t2[t2.index(x)] = "".join(x)
    for m in t2:
        t2[t2.index(m)] = chr(int(m,2))
    return "".join(t2)

if  __name__ == "__main__":
    if input("翻译输入1，反翻译输入2\n") == "1":
        print(encrypt(input("输入翻译后的语言\n喵语/叽咕语/自定义："),input("输入要翻译的文本\n")))
    else:
        print(decode(input("输入要反翻译的文本\n")))
    input()
