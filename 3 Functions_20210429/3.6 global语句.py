# 3.6 global语句
# 如果需要在一个函数内修改全局变量，就使用global语句


def spam():
	global eggs
	eggs = 'spam'


eggs = 'global'  # 在这里eggs还是'global'
spam()  # 这里调用spam函数把eggs变成了spam
print(eggs)

