a = int(input("введите a="))
k = input(" введите массив=")
arr = k.split()
s = int(arr[0])
for i in arr:
    if int(i) > s:
        s = int(i)
print("максимальное=", s)