# Sum of 'n' numbers
# Inputs: Two lines - number 'N' and these 'N' numbers in the following line.

# Using stdin and stdout
from sys import stdin, stdout


def main():
    print("Enter N value: ")
    n = stdin.readline()
    print("Enter the N numbers: ")
    arr = [int(x) for x in stdin.readline().split()]
    summation = 0
    for x in arr:
        summation += x
    print("Sum of N numbers: ")
    stdout.write(str(summation))


if __name__ == "__main__":
    main()
