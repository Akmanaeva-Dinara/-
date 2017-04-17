import math
a=float(input("введите а, не равное 0= "))
b=float(input("введите b= "))
c=float(input("введите c= "))
d = b**2 - 4*a*c
if d> 0:
	x1 = (-b + math.sqrt(d))/(2*a)
	x2 = (-b - math.sqrt(d))/(2*a)
	print("x1 =",x1, "x2 =", x2)
elif d == 0:
	x = -b/(2*a)
	print("x =", x)
else:
	print("Корней нет")
