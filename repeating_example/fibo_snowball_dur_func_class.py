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

class PhonemeSnowballGenerator:
    '''first: print a poem, where each line has a number of words corresponding to the fibonnaci sequence
        second: double that, so that the number of lines reflects our place in the fibonaccis sequence'''
    def __init__(self, phonemes, sentence, duration, time_growth,run_numb):
        self.phonemes = phonemes
        self.sent = sentence
        self.dur = duration
        self.tmgr = time_growth
        self.fib_list = [0,1, 1, 2, 3, 5]
        self.phrase = ''
        self.run_num = run_numb

    def ps(self, fib_list, dur, tmgr):
        for i in range(len(fib_list)):
            self.phrase = ''
            phrase = find_phonemes_ngram(-2, self.phonemes, sentence, i)
            rn = int(random.random()*len(phrase)-1)
            str_phrase = ' '.join(phrase[rn])
            self.phrase = self.phrase + str_phrase+" "
            self.ps2(fib_list, dur, tmgr, self.phrase)

    def ps2(self,fib, dur, tmgr, phrase):
        for i in fib:
            dur = dur * tmgr
            if i < 1:
                dur = 1
            print()
            for j in range(i):
                phrase = ''
                phr = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, i-1)
                rn = int(random.random()*len(phr)-1)
                no_punct_phrase = r_punct_list(phr[rn])
                str_phrase = ' '.join(no_punct_phrase)
                phrase = phrase + str_phrase+" "
                print(phrase)
            time.sleep(dur)

    def run_ps(self):
        for i in range(self.run_num):
            self.ps(self.fib_list, self.dur, self.tmgr)
            time.sleep(4)

pho_snow = PhonemeSnowballGenerator(phonemes, sentence,1,1.25,2)
pho_snow.run_ps()