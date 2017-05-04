s=input("введите предложение:")
n=len(s)
k=0;
mx=0;
for i in s:
    if i==' ':
        k=k+1
    elif mx<k:
        mx=k
        k=0
print('Максимальное количество пробелов подряд=',mx)
