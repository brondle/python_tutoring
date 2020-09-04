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


g = FP.phonemeList(num, phonemes, sentence)
z = refactored_find_phonemes(num, phonemes, sentence)
# print(z[50])

z = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, 5)
ph = FP.phonemeList_ngram(-2, ['AH0', 'N'], sentence, 3)

poem = ''

def ps(fib):
    for i in range(fib):
        ps.phrase = ''
        phrase = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, i)
        rn = int(random.random()*len(phrase)-1)
        str_phrase = ' '.join(phrase[rn])
        ps.phrase = ps.phrase + str_phrase+" "
        print(ps.phrase)

ps.phrase = ''

fibo_list = [0, 1, 1, 2, 3, 5, 8]
fibo_list2 =[0,1, 1, 2, 3]

def run_ps():
    for i in fibo_list:
        ps(i)
        print()

run_ps()
