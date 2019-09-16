# Creating a set

set1 = set()
print("Initial blank set: ")
print(set1)

set2 = set('Hello')
print("Set with the use of string: ")
print(set2)

String1 = 'Hello'
set3 = set(String1)
print("Set with the use of object: ")
print(set3)

set4 = set(["Hello", "World"])
print("Set with the use of lists: ")
print(set4)

set5 = set([1, 2, 3, 4, 5, 6, 7, 7, 7])
print("Set with the use of numbers: ")
print(set5)

set6 = set([1, 2, 'Hello', 3, 'World'])
print("Set with the use of mixed values: ")
print(set6)
