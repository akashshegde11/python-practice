# Unpacking of dictionary items using **


def fun(a, b, c):
    print(a, b, c)


d = {'a':2, 'b':4, 'c':10}
fun(**d)
