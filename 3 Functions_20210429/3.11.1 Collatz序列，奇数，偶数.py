#最终总会得到1的一个函数
def collatz(a) :
	if a%2 == 0:
	# %return余数，这行若ture则是偶数，若==1则是奇数
		return a//2 #return整除因子
	elif a %2 == 1 :
		return 3*a+1
		
while True:
	b= collatz( a=int(input() ) ) #若不把函数赋值给一个全局变量，函数执行完成后它就会把return值扔掉
	print(b)
	if b == 1:
		print('You got the 1')
		break
	else :
		continue



