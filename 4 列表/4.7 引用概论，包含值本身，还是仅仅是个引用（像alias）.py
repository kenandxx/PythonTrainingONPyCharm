#不可变数据类型的值：字符串，整型，元组。————变量保存值本身。
cat = 42
dog = cat
cat = 100
print(dog)
print(cat)


#可变数据类型的值：列表，字典。————-变量包含引用
spam = [0, 1, 2]
cheese = spam #这条命令执行后，spam和cheese就都指向了同一个ID的列表（或字典）
spam[1] = 'Hello'
print(cheese)
print(spam)
