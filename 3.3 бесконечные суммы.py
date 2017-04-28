n=int(input("введите n:"))
x=int(input("введите x:"))
fact=1
summa=1
s=1
for i in range(1,n+1):
    s=s*x
    fact=fact * i
    summa=summa + (s/fact)
print("summa=",summa)
