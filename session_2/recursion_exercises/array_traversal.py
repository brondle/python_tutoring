test_arr = [0, 1, 2, 3, 4]
def recursive_print(arr):
    print('arr: ', arr)
    if (len(arr) >= 1):
        print(arr[0])
        #how could we do this without passing a new version of the array, using indexing instead?
        recursive_print(arr[1:])

def recursive_print_with_index(array, i):
    if i > 0:
        recursive_print_with_index(array, i -1)
        print(array[i])

recursive_print_with_index(test_arr, len(test_arr) - 1)
