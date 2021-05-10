def spam(divideby):
		return 42/divideby
		
	
	
try:
	print(spam(2))
	print(spam(6))
	print(spam(0)) #error:divition by zero
	print(spam(1))	
except ZeroDivisionError:
	print('Error;Invalid argument.')

#如果把try except写在全局作用域，try遇到错之后的语句就不再执行了

#在运行try之后的子句如果出错，就立即跳转到运行except子句的代码
