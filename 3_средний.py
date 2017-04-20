k = int(input('k: '))
w = 0
i=-2
fac=-2+3
for i in range(-2,k) :
	w+=((-1)**i)*fac/(2*(i-4))
	fac*=i+3
	i+=1
print('Сумма =', w)
	
