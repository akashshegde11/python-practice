# Adding elements to a dictionary

dict1 = {}
print("Empty dictionary: ")
print(dict1)

dict1[0] = 'Geeks'
dict1[1] = 'for'
dict1[2] = 1
print("Dictionary after adding three elements: ")
print(dict1)

dict1['Value_set'] = 2, 3, 4
print("Dictionary after adding three more elements: ")
print(dict1)

dict1[1] = 'Welcome'
print("Updated key value: ")
print(dict1)

dict1[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
print("Adding a nested key: ")
print(dict1)
