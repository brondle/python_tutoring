from fp import FP
# import find_phoneme_oop
from fp import refactored_find_phonemes, find_phonemes_ngram
import repeating
import time
import nltk
import random
from nltk.tokenize import WhitespaceTokenizer, sent_tokenize
import re
prondict = nltk.corpus.cmudict.dict()

from nltk.tokenize import WhitespaceTokenizer, sent_tokenize
z = nltk.corpus.gutenberg.fileids()
f = open('artistStatements.txt')
raw2 = f.read()
sentence = sent_tokenize(raw2)
num = -2
phonemes = ['AH0', 'N']
# the arguments for find_phonemes_ngram are: the number of phonemes from the end, which phonemes, what string, how many words prior

# NEVER DECLARE THE SAME FUNCTION TWICE
def ps(ind, arr):
    for i in range(ind):
        ps.phrase = ''
        phrase = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, arr[i]-1)
        rn = int(random.random()*len(phrase)-1)
        str_phrase = ' '.join(phrase[rn])
        ps.phrase = ps.phrase + str_phrase+" "
        yield ps.phrase

ps.phrase = ''

#the ind argument is the number of index items before repeating
#arr is the list of items - an array, the fibonacci list

fibo_list = [1, 1, 2, 3, 5, 8]
fibo_list2 =[1, 1, 2, 3]

while True:
    for j in (ps(5, fibo_list)):
        print(j)
        time.sleep(2)
        print()


#Sept 3rd work with Brent
def ps_big(ind, arr):
    for i in range(ind):
        for j in range(i):
            ps_big.phrase = ''
            phrase = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, arr[i])
            rn = int(random.random()*len(phrase)-1)
            str_phrase = ' '.join(phrase[rn])
            ps_big.phrase = ps_big.phrase + str_phrase+" "
            yield ps_big.phrase
ps_big.phrase = ''




# while True:
#     for j in (ps_big(5, fibo_list)):
#         print(j)
#         time.sleep(1)
#
#

