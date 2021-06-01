import cmath
a = int(input("请输入二次项a：\n"))
b = int(input("请输入一次项b：\n"))
c = int(input("请输入常数项c：\n"))
result1 = (-b+cmath.sqrt(b**2-4*a*c))/(2*a)
result2 = (-b-cmath.sqrt(b**2-4*a*c))/(2*a)
print("解得ax**2+bx+c中的x为：{}或{}".format(result1,result2))