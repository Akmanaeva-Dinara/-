s=input("massiv:")
count=0
arr=s.split()
for i in range(len(arr)):
	arr[i]=int(arr[i])
for i in range(len(arr)):
        if arr[i]%2==0:
                count=count+1
print(count)
