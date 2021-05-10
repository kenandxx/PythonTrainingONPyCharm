spam = [1, 2, 3]
spam.append('Hello')
print(spam)


def egg(someparameter):
  someparameter.append('Hello')


ham = [1, 2, 3]
egg(ham)
# egg（ham）的隐含意义是：someparameter = ham
#一般来讲，函数是一用就破的，不会将return值保留。函数调用后，其return值会被删除，即不会对变量的结果产生影响。比如文末的change（）的调用并不会把b的值变成123.

#请注意，当egg被调用时，没有使用返回值来为ham赋予新值。相反，它直接当场就修改了ham列表。这就是为什么函数调用后仍然会对该列表产生影响

#尽管ham和someparameter包含了不同的引用，但是他们都指向了同样的列表。

print(ham)


#confirm
def change(a):
  a = 123
  print(a)


b = 456
change(b)  #OUT: 123
print(b)  #OUT: 456

