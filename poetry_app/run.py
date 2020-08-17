# from helpers.this_helper import gen_random_number
from helpers.rhymes import find_alliteration, gen_rando

import random, textwrap
import nltk
from textblob import TextBlob, Word
z = nltk.corpus.gutenberg.fileids()
f = open('artistStatements.txt')
raw = f.read()
f.close()
artBlob = TextBlob(raw)
sentences = artBlob.sentences
my_list = []


print(gen_rando())
find_alliteration(sentences,my_list)
# print('this is the function ', find_alliteration(sentences,my_list))
print(my_list)

#the function returns a list of tuples and it needs to be a string to use with the server app
# for i in range(len(my_list)):
#     print(' '.join(my_list[i]))


# print(gen_random_number())
# from my_helper import my_function
#
# print(my_function())



#choose a pair and convert it from a tuple to string
# my_tuple = gen_rhyme_pair()
# my1 = ' '.join(my_tuple[0])
# my2 = ' '.join(my_tuple[1])
# print(my1)
# print(my2)