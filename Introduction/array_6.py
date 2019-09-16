# Array - fromlist() and tolist()

import array

arr = array.array('i', [1, 2, 3, 1, 2, 5])
li = [1, 2, 3]

arr.fromlist(li)
print("Modified array: ", end='')
for i in range(0, len(arr)):
    print(arr[i], end=' ')

li2 = arr.tolist()
print('\r')
print("The new list created is: ", end='')
for i in range(0, len(li2)):
    print(li2[i], end=' ')
