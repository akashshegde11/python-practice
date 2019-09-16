# Slicing elements in a list

List1 = ['H', 'E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D']
print("Initial list: ")
print(List1)

List2 = List1[3:6]
print("Slicing elements in range 3-6: ")
print(List2)

List3 = List1[:-4]
print("Elements sliced till the 4th element from last: ")
print(List3)

List4 = List1[3:]
print("Elements sliced from 3rd element to the end: ")
print(List4)

List5 = List1[:]
print("Printing all elements using slicing: ")
print(List5)

List6 = List1[::-1]
print("Printing list in reverse: ")
print(List6)
