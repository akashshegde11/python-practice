# Illustration of main()


def get_integer():
    result = int(input("Enter a number: "))
    return result


def main():
    print("Hello!")
    output_var = get_integer()
    print("The number you have entered is: ", output_var)


if __name__ == "__main__":
    main()