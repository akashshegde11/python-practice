# Adding Elements to a List

List1 = []
print("Initial empty list: ", end='')
print(List1)

List1.append(1)
List1.append(2)
List1.append(3)
print("List after the addition of three numbers: ", end='')
print(List1)

for i in range(1, 4):
    List1.append(i)
print("List after addition of elements 1-3: ", end='')
print(List1)

List1.append((5, 6))
print("List after addition of a tuple: ", end='')
print(List1)

List2 = ['Hello', 'World']
List1.append(List2)
print("List after addition of a list: ", end='')
print(List1)

List1.insert(3, 12)
List2.insert(0, 'Hello')
print("List after performing insert operation: ", end='')
print(List1)

List1.extend([8, 'World', 'Always'])
print("List after performing extend operation: ", end='')
print(List1)

# Addition of single element - append

# Addition of multiple elements - extend
