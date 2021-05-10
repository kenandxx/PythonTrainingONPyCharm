# 方法和函数就是一回事，只是它是调用在一个值上。例如如果一个列表值储存在spam中，你就可以在这个列表上调用index（）这个列表方式
# 每组数据类型都有它自己的一组方法, 例如列表这个数据类型有一些有用的方法，用来查找，添加，删除或者操作列表中的值

spam = ['hello', 'hi', 'howdy', 'heyas','howdy'] #0,1,2,3,4
print(spam.index('hello'))
print(spam.index('hi'))
print(spam.index('howdy'))
print(spam.index('heyas'))



# 如果列表中存在重复的值，就返回第一次出现的下表。
print(spam.index('howdy'))
