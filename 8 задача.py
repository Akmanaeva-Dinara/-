k = input("введите массив=")
list = k.split()
a = 0
s = 0
while a < len(list)-1 and  not s:
    if ((int(list[a]) > 0 and
        int(list[a+1]) > 0) or
        (int(list[a]) < 0 and
         int(list[a+1]) < 0)):
        s = 1
    a+=1
if s:
    print("Есть")
else:
    print("Нет")