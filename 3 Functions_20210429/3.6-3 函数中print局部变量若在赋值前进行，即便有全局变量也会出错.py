#3.6-3 函数中print局部变量若在赋值前进行，即便有全局变量也会出错

eggs = 123

def pawn():
	print(eggs)
	eggs = 456

pawn()

#UnboundLocalError: local variable 'eggs' referenced before assignment
