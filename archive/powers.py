def powers(a, b):
    print('b: ', b)
    if b > 0:
        print('foo')
        print('b: ', b)
        print('a: ', a)

        return a*powers(a, b-1) #the b is the powers and the a is always five
    else: #once b is 0 we are returning 5
        print('outside loop')
        print('a: ', a)
        return a
print (powers(5, 3))


#a is increasing as it goes up