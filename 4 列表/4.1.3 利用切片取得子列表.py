spam = ['cat', 'bat', 'rat', 'elephant']

print(spam[0:0])
print(spam[0:1])
print(spam[0:2])
print(spam[0:3])
print(spam[0:4])


print('spam[:2] is:',spam[:1]) 
print('spam[1:] is:',spam[1:])#至最后一个
print('spam[:] is:',spam[:]) 

print(spam[0:-1]) #至倒数第一个的前一个 cat, bat, rat
print(spam[1:-1]) # bat, rat #从第二个到倒数第二个起来”””了”
print(spam[2:-1]) # rat
print(spam[3:-1]) # []
print(spam[4:-1]) # []

print('spam[0:-2] is',spam[0:-2]) # cat, bat
print('spam[0:-3] is',spam[0:-3]) # cat, bat
print('spam[-1:] is',spam[-1:]) # 从倒数第一个到最后一个elephant
print('spam[-1:-1] is',spam[-1:-1]) #从倒数第一个到倒数第二个
