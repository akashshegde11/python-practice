# Array - typecode, itemsize and buffer_info()

import array

arr = array.array('i', [1, 2, 3, 1, 2, 5])
print("The datatype of the array is: ", end=' ')
print(arr.typecode)

print("The itemsize of the array is: ", end=' ')
print(arr.itemsize)

print("The buffer_info of the array is: ", end=' ')
print(arr.buffer_info())
