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
    # this is going to do it once for each item in the fibonacci sequence
    # if we want to do it N times, we have to pass it N instead of the fibonnaci
    for i in range(len(fib)):
        ps.phrase = ''
        phrase = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, i)
        rn = int(random.random()*len(phrase)-1)
        str_phrase = ' '.join(phrase[rn])
        ps.phrase = ps.phrase + str_phrase+" "
        print ('second level iteration ', i)
        ps2(fib, dur, tmgr, ps.phrase)

#global variable to show us how many times it's iterating - do as i say, not as i do, etc
p_counter = 0
def ps2(fib, dur, tmgr, phrase):
    #here it loops through fib again - so it's not going infinitely, it's just going to do it for each element in the fibonnaci sequence *again* > which means it will do it 25 times for a 5 number sequence
    for i in fib:
        print('third level iteration: ', i)
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
            global p_counter
            print('phrase count', p_counter)
            p_counter += 1
            print(ps.phrase)
#        time.sleep(dur)

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
    # this is looping ps, which already squares the length of the fibonacci sequence, N times
    # so instead of 25, we get 75 runs
    for i in range(2):
        print('highest level iteration', i)
        ps(fibo_list2, 1, 1.25)
#        time.sleep(4)
#not sure why this is no longer stopping
run_ps()
