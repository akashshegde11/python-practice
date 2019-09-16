# Introduction to strings

a = "This is a string"
print(a)

L = [1, "a", "This is a string", 1+2]
print(L)
L.append(6)
print(L)
L.pop()
print(L)
print(L[1])

tup = (1, "a", "This is a string", 1+2)
print(tup)
print(tup[1])

i = 1
while i < 10:
    i += 1
    print(i, sep=' ', end='')

s = "This is a string"
print()
for i in s:
    print(i, sep=' ', end='')
print()
list_2 = [1, 4, 5, 6, 7, 8, 9]
for i in list_2:
    print(i, sep=' ', end='')
print()
for i in range(0, 10):
    print(i, sep=' ', end='')
print()
