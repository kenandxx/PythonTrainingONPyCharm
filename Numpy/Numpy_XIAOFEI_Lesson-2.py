import numpy as np
#创建数组
array1 = np.array([0,1,2,3])
#不仅列表可以，元祖也可以初始化
array2 = np.array((0,1,2,3))
#arrange(n), return 0 to n-1 list
array3 = np.arange(4)
#linspace(start, end, num) return from start to end, num個等間隔の数値
array4 = np.linspace(0,2*np.pi,3)

print("array1",array1)
print("array2",array2)
print("array3",array3)
print("array4",array4)

array5=np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])

#array property
print("Type",type(array5))
print("项类型",array5.dtype) #Int32
print("Array Size",array5.size) # row3*Col3=9
print("Shape",array5.shape)
print("项字节数",array5.itemsize) #8 bit is one byte, int32 is 8*4
print("数组维度",array5.ndim)
print("数组占用字节",array5.nbytes) #8 bit ＊ 9 items =72 bytes

#多维数组切片
print(array5[0,:2]) # =[0,0:2]

