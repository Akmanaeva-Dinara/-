from math import sqrt
a = []
n = int(input("Введите кол-во точек: "))
for i in range(n):
  a.append(input("Точка " + str(i+1) + ": ").split())
  a[i][0] = int(a[i][0])
  a[i][1] = int(a[i][1])
print(a)
maximum = 0
r_max = 0
c_max = []
for i in range(n-1):
  x1 = a[i][0]
  x2 = a[i+1][0]
  y1 = a[i][1]
  y2 = a[i+1][1]
  r = sqrt((x1 - x2)**2 + (y1 - y2)**2)/2
  c = [(x1+x2)/2, (y1+y2)/2]
  count = 0
  for j in range(n):
    x = a[j][0]
    y = a[j][1]
    if (x-c[0])**2 + (y-c[1])**2 == round(r**2, 2):
      count += 1
  if count > maximum:
    maximum = count
    r_max = r
    c_max = c
print("Радиус:",r_max)
print("Центр:",c_max)
