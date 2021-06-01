#正数平方根和负数平方根
import cmath
a = float(input("请输入一个正数：\n"))
b = float(input("请输入一个负数：\n"))
result1 = a**0.5
result2 = cmath.sqrt(b)
print("{}的平方根是{}".format(a,result1))
print("{}的平方根是{}".format(a,result2))