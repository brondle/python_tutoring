test_array = [0, 1, 2, 3]
test2 = '0123'

def map(arr, func):
    if len(arr) > 0:
        return [func(arr[0])] + map(arr[1:], func)
    else:
        return arr


def test_func(num):
    return num + 1

print(map(test_array, test_func))

