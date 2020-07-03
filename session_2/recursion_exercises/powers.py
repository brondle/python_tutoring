def powers(a, b):
    print('b: ', b)
    if b > 0:
        print('foo')
        return a*powers(a, b-1)
    else:
        return a
print (powers(5, 3))
