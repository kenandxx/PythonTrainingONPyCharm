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