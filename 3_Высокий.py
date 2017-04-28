n=int(input("введите n:"))
p=int(input("введите p:"))
Mp=(2**p)-1
print("Mp=",Mp)
i=2	
while i<=n:
    f=True
    j=2
    while f and j<i:
        if not i%j: f=False
        j+=1
    if f and i<Mp: print(i,' ')
    i+=1
   


