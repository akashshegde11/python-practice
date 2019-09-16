# Taking multiple inputs using lists


# Taking two inputs at a time
x, y = [int(x) for x in input("Enter two numbers: ").split()]
print("First number is: ", x)
print("Second number is: ", y)
print()

# Taking three inputs at a time
x, y, z = [int(x) for x in input("Enter three numbers: ").split()]
print("First number is: ", x)
print("Second number is: ", y)
print("Third number is: ", z)
print()

# Taking two inputs at a time, output using format()
x, y = [int(x) for x in input("Enter two numbers: ").split()]
print("The two numbers are: {} and {}".format(x, y))
print()

# Taking multiple inputs at a time, output using lists
x = [int(x) for x in input("Enter multiple values: ").split()]
print("Number of lists: ", x)
print()
