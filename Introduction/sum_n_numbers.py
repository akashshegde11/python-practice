# Sum of 'n' numbers
# Inputs: Two lines - number 'N' and these 'N' numbers in the following line.


# Basic method of input/output
n = int(input("Enter N value: "))
arr = [int(x) for x in input("Enter the numbers: ").split()]
summation = 0
for x in arr:
    summation += x
print(summation)
