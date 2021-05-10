import numpy as np
#新建数组
array = np.array([1,2,3])
print(type(array)) #nd means multi dimension, not only 1D array
print(array)

#Shape fun. shows How many rows, columns
#1D array
#[
#1,
#2,
#3,
#]
#2D array
#[
#[1,2],
#[3,4],
#[5,6],
#]

#


array = np.array(([[1,2],[3,4],[5,6]]))
print(array.shape) #result: (3,2) means 3rows 2cols
print(array[0]) #print row1
print(array[1]) #print row2
array[0] = -1   #grant -1 to [1,2]
print(array[0]) #print row1




#Multi-D array
Multi_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(Multi_array)
print(Multi_array.shape) #result (3, 3)

#Quickly create all 0 or 1 multi-D array
zeros_array = np.zeros((1,4)) #1row 4col
print(zeros_array)
ones_array = np.ones((2,4)) #1row 4col
print(ones_array)

#Fetch a factor:row1col2
print("Fetch a factor", Multi_array[0][2])
#Fetch a row:row1
print("Fetch a row",Multi_array[0,:])
#Fetch a col:col2
print("Fetch a col",Multi_array[:,2])

#数组操作
array1=np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
array2=np.array([[7,8,9],
                 [10,11,12],
                 [13,14,15]])
#数组相加
print("Add arrays\n",array1+array2)
print("Substract arrays\n",array1-array2)
print("Multiply arrays\n",array1*array2)
print("Divede arrays\n",array1/array2)
#矩阵乘法 Matrix multiplication
# https://en.wikipedia.org/wiki/Matrix_multiplication
print("Matrix multiplication\n",array1.dot(array2))
    #Result
    #Matrix multiplication
    #[[66=1*7+2*10+3*13  72=1*8+2*11+3*14  78=1*9+2*12+3*15]
    #[156 171 186]
    #[246 270 294]]

