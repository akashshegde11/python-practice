# Adding elements to a set

set1 = set()
print("Initial blank set: ")
print(set1)

set1.add(8)
set1.add(9)
set1.add(11)
print("Set after addition of three elements: ")
print(set1)

for i in range(1, 6):
    set1.add(i)
print("Set after the addition of elements in range 1-6: ")
print(set1)

set1.add((6, 7))
print("Set after the addition of a tuple: ")
print(set1)

set1.update([10, 11])
print("Set after the addition of elements using update: ")
print(set1)

# Addition of single element - add
# Addition of multiple elements - update
