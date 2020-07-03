test_arr = [0, 1, 2, 3, 4]
def recursive_print(arr):
    print('arr: ', arr)
    if (len(arr) >= 1):
        print(arr[0])
        #how could we do this without passing a new version of the array, using indexing instead?
        recursive_print(arr[1:])
recursive_print(test_arr)
