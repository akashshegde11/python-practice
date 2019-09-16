# Array - count() and extend()

import array

arr1 = array.array('i', [1, 2, 3, 1, 2, 5])
arr2 = array.array('i', [1, 2, 3])

print("The occurrences of 1 in array is: ", end='')
print(arr1.count(1))

arr1.extend(arr2)
print("Modified array: ", end='')
for i in range(0, len(arr1)):
    print(arr1[i], end=' ')
