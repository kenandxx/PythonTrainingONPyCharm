spam = ['cat', 'bat', 'rat', 'elephant']

spam[0] = 'dog'

print(spam)

spam[1] = spam[0]

print(spam) 

spam[-1] = 123456

print(spam) 

spam[0:1] = [1,2]
print(spam) 

spam[0:1] = [111111]
print(spam) 
