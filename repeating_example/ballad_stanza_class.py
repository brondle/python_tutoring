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
#ballad stanza aabccb

class BalladStanzaGenerator:
    def __init__(self, counter, phon_a, phon_b, phon_c):
        self.counter = counter
        self.conda = [0,1]
        self.condb = [2,5]
        self.condc = [3,4]
        self.phon_a = phon_a
        self.phon_b = phon_b
        self.phon_c = phon_c

    def get_ph_phrase(self, phon_type):
        phr = find_phonemes_ngram(-2, phon_type, sentence, 4)
        rn = int(random.random() * len(phr) - 1)
        no_punct_phrase = r_punct_list(phr[rn])
        str_phrase = ' '.join(phr[rn])
        return str_phrase

    def ballad_stanza(self, counter):
        if counter in self.conda:
            str_phrase = self.get_ph_phrase(phon_a)
            print(str_phrase)
        if counter in self.condb:
            str_phrase2 = self.get_ph_phrase(phon_b)
            print(str_phrase2)
        if counter in self.condc:
            str_phrase3 = self.get_ph_phrase(phon_c)
            print(str_phrase3)

    def run_ballad_stanza(self, counter):
        while counter < 6:
            if counter == 3:
                print()
                self.ballad_stanza(counter)
                time.sleep(2)
            else:
                self.ballad_stanza(counter)
                time.sleep(2)
            counter += 1
            if counter > 5:
                print()
                counter = 0

ballad = BalladStanzaGenerator(0, phon_a, phon_b,phon_c)
ballad.run_ballad_stanza(0)