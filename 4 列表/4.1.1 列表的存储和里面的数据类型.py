
['hello', 3.1415, True, None, 42]
spam = ['hello', 3.1415, True, None, 42]

print(spam)

print() #因为默认print后面有个换行符，所以什么都不打印其实就是打印了换行符

def listprint():
	while True:
		n = 0
		print(spam[n])
		n = n+1

listprint()


try:
	print(spam[0])
	print(spam[1])
	print(spam[2])
	print(spam[500])
	print(spam[3])
	print(spam[4])
	
except:
	print('printing list error')

print()

print(type(spam))
print(type(spam[0]))
print(type(spam[1]))
print(type(spam[2]))
print(type(spam[3]))
print(type(spam[4]))


