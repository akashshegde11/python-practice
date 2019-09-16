# Slicing of strings

String1 = "Hello World"
print("Initial String: ", end='')
print(String1)

print("First character of string: ", end='')
print(String1[0])

print("Last character of string: ", end='')
print(String1[-1])

print("Slicing characters from 4th character to the end: ", end='')
print(String1[3:])

print("Slicing characters between 4th and second-last character: ", end='')
print(String1[3:-2])

# Updating or deleting a character within a string is not allowed. Strings are immutable.

# Only new strings can be assigned to the same name.

# Deletion of entire string is possible using the 'del' keyword

String2 = "Hello World"
print("Case 2 - Initial String: ", end='')
print(String2)

String2 = "Cyberpunk"
print("Case 2 - Updated String: ", end='')
print(String2)

String3 = "Hello World"
print("Case 3 - Initial String: ", end='')
print(String3)

'''del String3
print("Case 3 - Deleted String: ", end='')
print(String3)'''
