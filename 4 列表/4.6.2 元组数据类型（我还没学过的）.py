eggs = ('hello', 
42,
0.5	)
print(eggs[0])
print(eggs[1:3]) #取值口诀：想要第几个到第几个？左减一，右加一。 例如：想要第三个到第五个。左减一：[3-1=2:] 右加一 [2:5+1]

#元组的值不能被改变
#eggs[1] = 999 #tuple object does not support item assignment

#如何让python知道这是tuple还是字符串
yuanzu = ('hello',)
string = ('hello')

print(type(yuanzu))
print(type(string))
