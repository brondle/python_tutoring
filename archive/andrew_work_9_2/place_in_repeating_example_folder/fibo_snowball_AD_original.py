from fp import FP
# import find_phoneme_oop
from fp import refactored_find_phonemes, find_phonemes_ngram
# from Find_phoneme import phoneme_list
# from find_phoneme import *
# from repeating import *
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



def ps(fib):
    for i in fib:
        time.sleep(2)
        for j in range(i):
            # print('j: ', j)
            ps.phrase = ''
            phrase = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, i-1)
            rn = int(random.random()*len(phrase)-1)
            str_phrase = ' '.join(phrase[rn])
            ps.phrase = ps.phrase + str_phrase+" "
            # we want to print i amount of times
            print(ps.phrase)

ps.phrase = ''

fibo_list = [0, 1, 1, 2, 3, 5, 8]
fibo_list2 =[0,1, 1, 2, 3]

# first: print a poem, where each line has a number of words corresponding to the fibonnaci sequence

#second: double that, so that the number of lines reflects our place in the fibonaccis sequence

def run_ps():
    #if we want to loop it N times
    for i in range(4):
        ps(fibo_list)
        #sleep in between runs
        print()

run_ps()
