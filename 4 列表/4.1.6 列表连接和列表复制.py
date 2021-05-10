list1 = [1, 2, 3] 
list2 = ['a', 'b', 'c']

print(list1+list2)
print(list2*3)

del list2[0]
print(list2)

del list2[0:1]
print(list2)

del list2[0:]
print(list2)

del list2[:]
print(list2)
