s=str(input("введите строку:"))
k=0
for i in s:
	if i=="А":
		k=k+1
if k==0:
        print("заглавной буквы А нет")
else:
        print(k)
