spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)

spam.insert(0, 'first') #第一个参数是插入位置，第二个是插入值
print(spam)

#请注意，其实append（）和insert（）的返回值是None。所以不应该写作 spam = spam.append('moose')



