# Packing of dictionary items using **


def fun(**kwargs):
    print(type(kwargs))
    for key in kwargs:
        print("%s = %s" % (key, kwargs[key]))


fun(name="GFG", ID="101", language="Python")
