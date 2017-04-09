import math
a=int(input("введите а="))
x=int(input("введите х="))
c=int(input("введите с="))
L=(math.sqrt(math.exp(x))-math.cos((x**2)*(a**5))**4)+(math.atan(a-(x**5))**4)/(math.exp((math.sqrt(math.fabs(a+(x*(c**4)))))))
print(L)

