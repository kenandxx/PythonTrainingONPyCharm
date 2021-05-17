spam = {'color': 'red', 'age': 42}
a = list(spam.keys())
print(a[0])

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
print('******Stocking fashion test******')
itemdic = {'Lisa':{'Apple':3, 'Pear':5}, 'Ken':{'Cake':100, 'Coke':5} }
for k, v in itemdic.items():
	print('Key:' + k + ' Value: '+ str(v))
	print(v.get('Apple','Noneforyou'))
	Lista = list(v)
	for i in range(0, len(Lista)): # 0,1 execute
		print(Lista[i])
		print(v.get(Lista[i],'Noneforyou')) #超出列表下标范围会Index Error

	# print(v.get(v.keys(),'Noneforyou')) # 这个行不通，需要自己输入key,或者list化

