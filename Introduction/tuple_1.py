# Creating a tuple

Tuple1 = ()
print("Initial empty tuple: ")
print(Tuple1)

Tuple2 = ('Geeks', 'for')
print("Tuple with the use of string: ")
print(Tuple2)

List1 = [1, 2, 3, 4, 5]
print("Tuple using list: ")
print(tuple(List1))

Tuple3 = 'Geeks'
n = 5
print("Tuple with a loop")
for i in range(int(n)):
    Tuple3 = (Tuple3, )
    print(Tuple3)

Tuple4 = tuple('Geeks')
print("Tuple with the use of function: ")
print(Tuple4)

Tuple5 = (5, 'Welcome', 7, 'geeks')
print("Tuple with mixed data types: ")
print(Tuple5)

Tuple6 = (0, 1, 2, 3)
Tuple7 = ('python', 'hello')
Tuple8 = (Tuple6, Tuple7)
print("Tuple with nested tuples: ")
print(Tuple8)

Tuple9 = ('Geeks', ) * 3
print("Tuple with repetition: ")
print(Tuple9)
