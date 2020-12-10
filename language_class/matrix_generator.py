from itertools import product
def binary_matrix_generator(length):
    binary = [0, 1]
    return product(binary, repeat=length)

print(len(list(binary_matrix_generator(6))))

