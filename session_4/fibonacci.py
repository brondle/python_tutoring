#num is the how many numbers into the fibonacci sequence do you want to go

def fibonacci(num):
    a = 0
    b = 1
    for i in range(num):
        print(b)
        a, b = b, a + b

obj = fibonacci(6)
print('\n')

#generator version with yield. This one keeps a tally of what the last b that was called.
def fibonacciGenerator(num):
    a = 0
    b = 1
    for i in range(num):
        yield b
        a, b = b, a + b

# print(next(obj))
obj = fibonacciGenerator(6)

for i in range(6):
    print(next(obj))

#The next() function returns the next item from the iterator.
#next(iterator, default)
#iterator - next() retrieves next item from the iterator
#default (optional) - this value is returned if the iterator is exhausted (there is no next item)
print('\n')
words = ['I', 'me', 'mine', 'this', 'that', 'other', 'impossible']
words2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']

it = len(words)
def fibo_words():
    for i in range(it):
        # yield words[i], words2[i]
        # print(b)
        a, b = words2[i], words[i] + " " + words2[i]
        print(a, b)
        # return a, b

fibo = fibo_words()
print('\n')

a = ' '
b = ' '

def fibo_one_word_list():
    for i in range(it-1):
        yield a, b
        a, b = words[i+1], words[i] + " " + words[i+1]

        print(a, b)
        # return a, b

fibo = fibo_one_word_list()

print('\n')
y = ''
z = ''
my_letters = []
my_letters2 = []

def fibo_char_multiplier(num):
    a = 0
    b = 1
    for i in range(num):
        yield b
        a, b = b, a + b
        z = a*'a'
        y = b*'b'
        my_letters.append(z)
        my_letters2.append(y)
        # return(z, y)
        # print(z)
        # print(y)

# print(next(obj))
char_obj = fibo_char_multiplier(6)

for i in range(6):
    # print(next(char_obj))
    next(char_obj)
print(my_letters)
print(my_letters2)

print(my_letters2[len(my_letters2)-1] + my_letters[len(my_letters)-1])
print(my_letters[len(my_letters)-1])