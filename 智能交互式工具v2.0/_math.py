class Math():
    def __init__(self):
        try:
            name = input("想要计算的类型(支持计算长方形，正方形，长方体，\n正方体，三角形，平行四边形，梯形，圆和圆柱)：")
            if name == '长方形':
                a = float(input("请输入长方形的长："))
                b = float(input("请输入长方形的宽："))
                C = (a + b) * 2
                S = a * b
                print("长方形的周长为" + str(C))
                print("长方形的面积为" + str(S))

            elif name == '正方形':
                a = float(input("请输入正方形的边长："))
                C = a * 4
                S = a * a
                print("正方形的周长为：" + str(C))
                print("正方形的面积为：" + str(S))

            elif name == '正方体':
                a = float(input("请输入正方体的棱长："))
                V = a ** 3
                表S = a * a * 6
                print("正方体的体积为：" + str(表S))
                print("正方体的体积为：" + str(V))

            elif name == '长方体':
                A = float(input("请输入长方体的长:"))
                B = float(input("请输入长方体的宽:"))
                H = float(input("请输入长方体的高:"))
                S = (A * B + A * H + H * B) * 2
                V = A * B * H
                print("长方体的表面积是：" + str(S))
                print("长方体的体积是：" + str(V))

            elif name == '圆柱':
                R = float(input("请输入圆柱底面半径："))
                H = float(input("请输入圆柱的高："))
                底面C = R * 2 * 3.14  # 计算圆柱的底面周长
                侧S = 底面C * H  # 计算圆柱的侧面积
                底面S = R ** 2 * 3.14  # 计算圆柱的底面积
                表S = 底面S * 2 + 侧S  # 计算圆柱的表面积
                V = 底面S * H  # 计算圆柱的体积
                print("圆柱的底面周长是：" + str(底面C))  # 输出函数
                print("圆柱的侧面积是：" + str(侧S))  # 输出函数
                print("圆柱的底面积是：" + str(底面S))  # 输出底面积函数
                print("圆柱的表面积是：" + str(表S))  # 输出表面积函数
                print("圆柱的体积是：" + str(V))  # 输出函数

            elif name == '圆':
                R = float(input("请输入圆的半径："))
                S = R ** 2 * 3.14  # 计算圆的面积
                D = R * 2  # 计算圆的直径
                C = D * 3.14  # 计算圆的周长
                print("圆的面积是:" + str(S))
                print("圆的直径为：" + str(D))
                print("圆的周长为：" + str(C))

            elif name == '三角形':
                A = float(input("请输入三角形的底："))
                H = float(input("请输入三角形的高："))
                S = A * H / 2
                print("三角形的面积是：" + str(S))

            elif name == '平行四边形':
                A = float(input("请输入平行四边形的底："))
                H = float(input("请输入平行四边形的高："))
                S = H * A
                print("平行四边形的面积为：" + str(S))

            elif name == '梯形':
                a = float(input("请输入梯形的上底："))
                b = float(input("请输入梯形的下底;"))
                h = float(input("请输入梯形的高："))
                S = (a + b) * h / 2
                print("梯形的面积是：" + str(S))

            else:
                print("<暂不支持计算该类型>\n")

        except:
            print("<无效的输入>\n")
