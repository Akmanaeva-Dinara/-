s=str(input("введите строку:"))
a=s.split()
a[0],a[len(a)-1]=a[len(a)-1],a[0]
s=" ".join(a)
print(s)
