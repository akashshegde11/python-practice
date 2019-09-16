# Deleting elements from a dictionary

dict1 = {5: 'Welcome', 6: 'to', 7: 'Geeks',
         'A': {1: 'Geeks', 2: 'for', 3: 'Geeks'},
         'B': {1: 'Geeks', 2: 'Life'}}

print("Initial dictionary: ")
print(dict1)

del dict1[6]
print("Deleting a specific key: ")
print(dict1)

del dict1['A'][2]
print("Deleting a key from a nested dictionary: ")
print(dict1)

dict1.pop(5)
print("Popping a specific element: ")
print(dict1)

dict1.popitem()
print("Popping an arbitrary key-value pair: ")
print(dict1)

dict1.clear()
print("Deleting entire dictionary: ")
print(dict1)
