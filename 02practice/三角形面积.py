a = float(input("请输入第一边长：\n"))
b = float(input("请输入第二边长：\n"))
c = float(input("请输入第三边长：\n"))

p = (a+b+c)/2   #半周长
s = (p*(p-a)*(p-b)*(p-c))**0.5 #海伦公式
print("三角形面积为：{}\n".format(s))

