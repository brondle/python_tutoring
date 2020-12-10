test_array = [0, 1, 2, 3]
test2 = '0123'

def map(arr, func):
    print('arr is ', arr, 'len of arr is ', len(arr))
    if len(arr) > 0:
        print('func arr[0] is', func(arr[0]))
        return [func(arr[0])] + map(arr[1:], func)
    else:
        print('in the else now', arr)
        return arr


def test_func(num):
    print('test function is called and the number is ', num)
    return num + 1

print(map(test_array, test_func))
print('\n')

he = ['stuttered', 'lingered', 'winced', 'stumbled','dove']


words = ['one', 'two', 'three', 'four']
jj_nn = ['social engagement', 'institutional critique', 'activist art', 'urban life', 'everyday life', 'rigorous absurdity', 'traditional design', 'public space', 'artificial intelligence', 'biometric sensing', 'personal narrative',\
         'radical personhood', 'digital technology', 'digital art', 'systematic violence', 'feminist discourse', 'prosumer technology', 'contemporary life', 'further dialog', 'sublte manipulation', 'theoretical research', 'whole imagery', \
         'multi-channel video', 'multi-channel audio', 'hand-drawn rotoscoping', 'sound installation', 'cultural hybridity', 'popular culture', 'lush visuality', 'visual music', 'emotional expression', 'archival material', 'capitalist production','non-repesentational drawing', 'feminist art']

def map2(arr, func):
    print('arr is ', arr, 'len of arr is ', len(arr))
    if len(arr) > 0:
        print('func arr[0] is', func(arr[0]))
        return [func(arr[0])] + map2(arr[1:], func)
    else:
        print('in the else now', arr)
        return arr

def test_func2(word):
    print('test function is called ', word)
    return word + ' and '

print(map2(jj_nn[:5], test_func2))
#you could use this to create new lists from a set batch of text with interesting prepends and appends
print('\n')
new_combined_list = map2(jj_nn, test_func2)
def converttostr(input_seq, seperator):
   # Join all the strings in list
   final_str = seperator.join(input_seq)
   return final_str

# List of words names separated with a space
seperator = ''
print('My work examines', converttostr(new_combined_list[:5], seperator), 'peaceful resistance to illuminate', converttostr(new_combined_list[6:9], seperator), 'to change the world for good.' )

