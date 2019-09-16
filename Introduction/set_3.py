# Removing elements from a set

set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Initial set: ")
print(set1)

set1.remove(5)
set1.remove(6)
print("Set after removing two elements: ")
print(set1)

set1.discard(8)
set1.discard(5)
print("Set after discarding two elements: ")
print(set1)

for i in range(1, 5):
    set1.remove(i)
print("Set after removing a range of elements: ")
print(set1)

set1.pop()
print("Set after popping an element: ")
print(set1)

set1.clear()
print("Set after clearing all the elements: ")
print(set1)

# remove - KeyError arises if element does not exist in set
# discard - KeyError does not arise if element does not exist in set
# pop - removes last element of the set
# clear - removes all elements from a set
