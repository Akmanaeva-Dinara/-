import math
x=int(input("x="))
y=int(input("y="))
s1=0
s2=0
if ((x>0) and (y>0)):
   s1=x
   s2=y
elif ((x<0) and (y>0)):
            s1=x*(-1)
            s2=y
elif ((x>0) and (y<0)):
              s2=y*(-1)
              s1=x
elif (x<0) and (y<0):
             s1=x*(-1)
             s2=y*(-1)
p=(s1+s2)/2
q=math.sqrt(s1*s2)
print('Полусумма равна ',p);
print('Квадратный корень из произведения равен ',q);
