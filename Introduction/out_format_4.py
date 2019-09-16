# Output using format - Part 3

tab = {'geeks': 4127, 'for': 4098, 'geek': 87119}

print('Geeks: {0[geeks]:d}, For: {0[for]:d}, Geeks: {0[geek]:d}'.format(tab))

data = dict(fun="GeeksForGeeks", adj="Portal")

print("I love {fun} computer {adj}".format(**data))
