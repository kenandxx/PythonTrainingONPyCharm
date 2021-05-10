spam = 42
spam = spam +1 #43
print(spam)

spam += 1	#44
print(spam)

spam -= 4	#40
print(spam)

spam *= 2 #80
print(spam)

spam /= 20 #4
print(spam)

spam %= 3 #余数是1
print(spam)

ham = 'Hello' #也可以实现字符间的链接
ham += ' world'
print(ham)

cat = ['Honey'] #也可以实现列表的复制
cat *= 3
print(cat)

cat += ham
print(cat)

cat += [ham]
print(cat)
