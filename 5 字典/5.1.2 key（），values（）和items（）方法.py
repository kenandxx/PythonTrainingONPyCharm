spam = {'color': 'red', 'age': 42}

	
for a in spam.keys(): #键
	print('keys():',a)

print()	

for v in spam.values(): #值
	print('values():',v)

print()	

for i in spam.items(): #键-值对，返回的是键的元组和值的元组
	print('items():',i)
	
#如果需要返回一个列表，则使用list（）

A = list(spam.keys())
print(type(A))
print(A)

#也可以使用多重赋值技巧，在for循环中将键和值分别赋值给不同的变量。

for k, v in spam.items():
	print('Key:' + k + ' Value: '+ str(v))
