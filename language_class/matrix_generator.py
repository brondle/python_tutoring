from itertools import product
def binary_matrix_generator(length):
    binary = [0, 1]
    return product(binary, repeat=length)

# print(len(list(binary_matrix_generator(6))))

print(list(binary_matrix_generator(6)))

the_matrix = list(binary_matrix_generator(6))

for i in the_matrix:
    print(i)

