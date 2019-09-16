# Taking multiple inputs at a time


# Two inputs at a time
x, y = input("Enter two numbers: ").split()
print("Number of 1's: ", x)
print("Number of 0's: ", y)
print()

# Three inputs at a time
x, y, z = input("Enter three numbers: ").split()
print("Number of red lines: ", x)
print("Number of green lines: ", y)
print("Number of blue lines: ", z)
print()

# Taking two inputs, output using 'format'
x, y = input("Enter two numbers: ").split()
print("First number is {} and second number is {}".format(x, y))
print()

# Multiple inputs, using list
x = list(map(int, input("Enter multiple values: ").split()))
print("List of numbers: ", x)
