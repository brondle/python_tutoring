from itertools import product, permutations, combinations
def binary_matrix_generator(length):
    binary = [0, 1]
    return product(binary, repeat=length)

# print(len(list(binary_matrix_generator(6))))
#
# print(list(binary_matrix_generator(6)))

the_matrix = list(binary_matrix_generator(6))

# for i in the_matrix:
#     print(i)




#ex of simple product
a = [1,2,3,4]
b = ['a','b','c']

# for i in product(a,b):
#     print(i)

phn_list = [['DH', 'AH0'], ['K', 'AE1', 'CH'], ['IH1', 'Z'], ['DH', 'AH0'], ['L', 'AE1', 'G'], ['B', 'IH0', 'T', 'W', 'IY1', 'N'], ['T', 'UW1'], ['K', 'AY1', 'N', 'D', 'Z'],  ['AH1', 'V'], ['N', 'AA1', 'L', 'AH0', 'JH']]
only_phones = ['DH', 'AH0', 'K', 'AE1', 'CH', 'IH1', 'Z','DH', 'AH0', 'L', 'AE1', 'G', 'B', 'IH0', 'T', 'W', 'IY1', 'N', 'T', 'UW1', 'K', 'AY1', 'N', 'D', 'Z',  'AH1', 'V', 'N', 'AA1', 'L', 'AH0', 'JH']

only_unique_phones = ['DH', 'AH0', 'K', 'AE1', 'CH', 'IH1', 'Z', 'L', 'G', 'B', 'IH0', 'T', 'W', 'IY1', 'N', 'UW1', 'AY1', 'D',  'AH1', 'V', 'AA1','JH']


def permut(length):
    return permutations(phn_list, r=length)

# print(list(permut(2)))

def combo(ln):
    return combinations(only_unique_phones, r=ln)

print(list(combo(2)))
