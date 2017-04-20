from math import sin
x=0.1
print('x   -   y')
while x<=2.1:
      y=x**2+sin(5*x)
      print(round(x,2),'-', round(y,2))
      x += 0.2
	
