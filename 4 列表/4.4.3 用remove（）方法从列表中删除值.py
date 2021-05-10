spam = ['cat', 'dog', 'bat', 'elephant']
spam.remove('bat')
print(spam)

try:
	spam.remove('mouse')
except :
	print('error')
# ValueError: list.remove(x): x not in list

#如果有好几个同样的列表项，则只有第一个会被删除
spam = ['cat', 'dog', 'bat', 'elephant','cat']
spam.remove('cat')
print(spam)
del spam[0] #第一个删除
print(spam)

spam = ['cat', 'dog', 'bat', 'elephant','cat']
del spam[0:3] #第一个到第三个删除
print(spam)
