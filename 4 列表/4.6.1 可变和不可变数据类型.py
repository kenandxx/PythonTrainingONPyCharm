name = 'I love little girl'
print(name[7]) # out is l
# name[7] = 'L'	# Error: 'str' object does not support item assignment

newname = name[0:7] + 'big ' + name[-4:]
print(newname)

#如果你确实需要改变eggs中原来的值，你要这么做
eggs= [1,
2,
3]

print(eggs)

