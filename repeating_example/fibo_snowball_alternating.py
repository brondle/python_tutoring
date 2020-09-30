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
phon_a = ['AH0', 'N']
phon_b = ['AH0', 'L']
phon_c = ['AW1', 'ER0']


short_stack = sentence[:50]
# my_list = short_stack.split()

# for i in short_stack:
#     s = i.split()
#     for j in range(len(s)):
#         if s[j] in prondict:
#             silly = prondict[s[j]]
#             print(s[j], silly)


def ps(fib):
    for i in range(len(fib)):
        ps.phrase = ''
        phrase = find_phonemes_ngram(-2, phon_a, sentence, i)
        phrase2 = find_phonemes_ngram(-2, phon_b, sentence, i)
        rn = int(random.random()*len(phrase)-1)
        rn2 = int(random.random()*len(phrase2)-1)
        str_phrase = ' '.join(phrase[rn])
        str_phrase2 = ' '.join(phrase2[rn2])
        ps.phrase = ps.phrase + str_phrase+" "
        ps.phrase2 = ps.phrase2 + str_phrase2+" "
        dur = 1
    for i in fib:
        dur = dur * 1.25
        if i < 1:
            dur = 1
        print()
        for j in range(i):
            if j % 2 == 0:
                # print('i is ', i, ' print j is ', j)
                ps.phrase = ''
                phrase = find_phonemes_ngram(-2, phon_a, sentence, i-1)
                rn = int(random.random()*len(phrase)-1)
                no_punct_phrase = r_punct_list(phrase[rn])
                str_phrase = ' '.join(no_punct_phrase)
                ps.phrase = ps.phrase + str_phrase + " "
                print(ps.phrase)

            else:
                ps.phrase2 = ''
                phrase2 = find_phonemes_ngram(-2, phon_b, sentence, i-1)
                rn2 = int(random.random() * len(phrase2)-1)
                no_punct_phrase2 = r_punct_list(phrase2[rn2])
                str_phrase2 = ' '.join(no_punct_phrase2)
                ps.phrase2 = ps.phrase2 + str_phrase2 + " "
                print(ps.phrase2)
        time.sleep(dur)

ps.phrase = ''
ps.phrase2 = ''

fibo_list = [0, 1, 1, 2, 3, 5, 8]
fibo_list2 =[0,1, 1, 2, 3, 5]

# ps(fibo_list2)

# first: print a poem, where each line has a number of words corresponding to the fibonnaci sequence
#second: double that, so that the number of lines reflects our place in the fibonaccis sequence
#third: make each line alternate between one kind of phoneme or another

def run_ps():
    # for i in fibo_list:
    #     ps(i)
    #     print()
    #if we want to loop it N times
    for i in range(3):
        ps(fibo_list2)
        # print('this is the run_ps four second pause')
        time.sleep(4)

run_ps()