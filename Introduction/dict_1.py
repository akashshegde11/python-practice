# Creating a dictionary

dict1 = {}
print("Empty dictionary: ")
print(dict1)

dict2 = {1: 'Geeks', 2: 'for', 3: 'Geeks'}
print("Dictionary with the use of integer keys: ")
print(dict2)

dict3 = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("Dictionary with the use of mixed keys: ")
print(dict3)

dict4 = dict({1: 'Geeks', 2: 'for', 3: 'Geeks'})
print("Dictionary with the use of dict(): ")
print(dict4)

dict5 = dict([(1, 'Geeks'), (2, 'For')])
print("Dictionary with each item as a pair: ")
print(dict5)

dict6 = {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'Hello'}}
print("Nested dictionary: ")
print(dict6)
