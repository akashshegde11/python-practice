# Removing items from a list

List1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("Initial list: ", end='')
print(List1)

List1.remove(5)
List1.remove(7)
print("List after removing two elements: ")
print(List1)

for i in range(3, 5):
    List1.remove(i)
print("List after removing a range of elements: ")
print(List1)

List1.pop()
print("List after popping an element:")
print(List1)

List1.pop(4)
print("List after popping a specific element: ")
print(List1)
