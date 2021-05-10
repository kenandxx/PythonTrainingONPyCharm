spam = ['hello', 3.1415, True, None, 42]

print(spam)

print() #因为默认print后面有个换行符，所以什么都不打印其实就是打印了换行符

def listprint():
	
	Num = 1
	while Num<=10:
		try:
			n = 0 #因为每次执行while循环都先把n弄成了零，末尾给它加1也没用
			print(str(Num) +'time print :'+ spam[n])
			n = n+1
			Num = Num+1
		except :
			print('The whole list has been printed out')
			break

listprint()
