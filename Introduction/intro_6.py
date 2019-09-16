# Use of absolute function in Math library


import math


def main():
    num = float(input("Enter a decimal number: "))
    num = math.fabs(num)
    print(num)


if __name__ == '__main__':
    main()