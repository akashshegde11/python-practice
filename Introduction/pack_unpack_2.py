# Packing and unpacking


def fun1(a, b, c):
    print(a, b, c)


def fun2(*args):
    args = list(args)
    args[0] = 'GFG'
    args[1] = 'Awesome'
    fun1(*args)


fun2('Hello', 'Beautiful', 'World')
