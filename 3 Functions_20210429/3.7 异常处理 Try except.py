def spam(divideby):
	try:
		return 42/divideby
	except:
	#except ZeroDivisionError: #ZeroDivisionError是一个Python预设值，
		print('Error;Invalid argument.')
	#在运行try之后的子句如果出错，就立即跳转到运行except子句的代码
	
	
print(spam(2))
print(spam(6))
print(spam(0)) #error:divition by zero
print(spam(1))
