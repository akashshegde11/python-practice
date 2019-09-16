# Demo of packing and unpacking


def fun(a, b, c, d):
    print(a, b, c, d)


my_list = [1, 2, 3, 4]

# This will not work because the function takes 4 arguments
# fun(my_list)

''' This will work because '*' unpacks the list and all elements are passed
    as parameters to the function
'''
fun(*my_list)


def my_sum(*args):
    sum_n = 0
    for i in range(0, len(args)):
        sum_n += args[i]
    return sum_n


print(my_sum(1, 2, 3, 4, 5))
print(my_sum(10, 20))
