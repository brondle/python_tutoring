from fp import FP
from fp import r_punct_list
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

def ps(fib, dur, tmgr):
    for i in range(len(fib)):
        ps.phrase = ''
        phrase = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, i)
        rn = int(random.random()*len(phrase)-1)
        str_phrase = ' '.join(phrase[rn])
        ps.phrase = ps.phrase + str_phrase+" "
        ps2(fib, dur, tmgr, ps.phrase)

def ps2(fib, dur, tmgr, phrase):
    for i in fib:
        dur = dur * tmgr
        if i < 1:
            dur = 1
        print()
        for j in range(i):
            ps.phrase = ''
            phrase = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, i-1)
            rn = int(random.random()*len(phrase)-1)
            no_punct_phrase = r_punct_list(phrase[rn])
            str_phrase = ' '.join(no_punct_phrase)
            ps.phrase = ps.phrase + str_phrase+" "
            print(ps.phrase)
        time.sleep(dur)

ps.phrase = ''

fibo_list = [0, 1, 1, 2, 3, 5, 8]
fibo_list2 =[0,1, 1, 2, 3, 5]

# first: print a poem, where each line has a number of words corresponding to the fibonnaci sequence
#second: double that, so that the number of lines reflects our place in the fibonaccis sequence

def run_ps():
    # for i in fibo_list:
    #     ps(i)
    #     print()

    #if we want to loop it N times
    for i in range(2):
        ps(fibo_list2, 1, 1.25)
        time.sleep(4)
#not sure why this is no longer stopping
run_ps()