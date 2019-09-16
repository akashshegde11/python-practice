# Array operations - pop() and remove()

import array

arr = array.array('i', [1, 2, 3, 1, 5])
print("The newly created array: ", end=' ')
for i in range(0, 5):
    print(arr[i], end=' ')

print('\r')

arr.pop(2)
print("The array after popping an element: ", end=' ')
for i in range(0, 4):
    print(arr[i], end=' ')

print('\r')

arr.remove(1)
print("The array after removing an element: ", end=' ')
for i in range(0, 3):
    print(arr[i], end=' ')
