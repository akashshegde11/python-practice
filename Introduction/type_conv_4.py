# Type conversion using dict(), complex(), str()

a = 1
b = 2

tup = (('a', 1), ('f', 2), ('g', 3))

c = complex(1, 2)
print("After converting integer to complex number: ", end='')
print(c)

c = str(a)
print("After converting integer to string: ", end='')
print(c)

c = dict(tup)
print("After converting tuple to dictionary: ", end='')
print(c)
