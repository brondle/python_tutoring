#in-class examples Friday, July 3rd

test_arr = [0, 1, 2, 3, 4]
def recursive_print(arr):
    print('arr: ', arr)
    if (len(arr) >= 1):
        print(arr[0])
        #how could we do this without passing a new version of the array, using indexing instead?
        recursive_print(arr[1:])
recursive_print(test_arr)

print('\n')

def recursive_print_with_index(array, i):
    if i > 0:
        recursive_print_with_index(array, i -1)
        print(array[i])
recursive_print_with_index(test_arr, len(test_arr) - 1)
print('\n')

my_text = ["this", "that", "one", "yes", "no", "maybe", "sure"]
text = []
def recrusive_words(word_list, i):
    if i > 0:
        recrusive_words(word_list, i-1)
        print(word_list[i])
recrusive_words(my_text, len(my_text) - 1)
print('\n')
def combine(word_list, i):
    out = []
    if i > 0 and len(word_list)>=i:
        print('i is ', i)
        if i == 1:
            out = out + [[word_list[0]]]
        else:
            out = out + combine(word_list[1:], i -1)
        out = out + combine(word_list[1:], i)
        print(out)
    return out
print('\n')
print('last line of code')
combine(my_text, len(my_text)-1)