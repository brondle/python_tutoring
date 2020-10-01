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

short_stack = sentence[:50]

# def show_me_phonemes(sentence):
#     for i in sentence:
#         s = i.split()
#         for j in range(len(s)):
#             if s[j] in prondict:
#                 syl = prondict[s[j]]
#                 print(s[j], syl)

conda = [0,1]
condb = [2,5]
condc = [3,4]

def ballad_stanza(counter):
    # print("counter is ", counter)
    print('counter: ', counter)
    if counter in conda:
    # if counter == 0 or 1: #why didn't this combo of if/elif work? it just kept going with the first condition
    #     print('we are in cond1 ')
        ballad_stanza.phrase = ''
        phrase = find_phonemes_ngram(-2, phon_a, sentence, 4)
        rn = int(random.random() * len(phrase) - 1)
        no_punct_phrase = r_punct_list(phrase[rn])
        str_phrase = ' '.join(phrase[rn])
        print(str_phrase)
    # if counter in condb:
    elif counter == 2 or 5:
    #     print('we are in cond2 ')
    # 2 or 5 will always evaluate to 2 - we're not comparing true or false values there, it's just going to give the first value because it "exists" according to the code
    # we have to separate out the evaluations, like counter == 2 or counter == 5 (the best way to do this is with a tuple> if counter in (2, 5))
        print('what now', (2 or 5))
        ballad_stanza.phrase2 = ''
        phrase2 = find_phonemes_ngram(-2, phon_b, sentence, 4)
        rn2 = int(random.random() * len(phrase2) - 1)
        no_punct_phrase2 = r_punct_list(phrase2[rn2])
        str_phrase2 = ' '.join(no_punct_phrase2)
        print(str_phrase2)
    if counter in condc:
    # elif counter == 3 or 4:
    #     print('we are in cond3 ')
        ballad_stanza.phrase3 = ''
        phrase3 = find_phonemes_ngram(-2, phon_c, sentence, 4)
        rn3 = int(random.random() * len(phrase3) - 1)
        no_punct_phrase3 = r_punct_list(phrase3[rn3])
        str_phrase3 = ' '.join(no_punct_phrase3)
        print(str_phrase3)

ballad_stanza.phrase1 = ''
ballad_stanza.phrase2 = ''
ballad_stanza.phrase3 = ''

# ballad_stanza(count)
c = 0

#simple version
def run_ballad(c):
    while c < 6:
        ballad_stanza(c)
        time.sleep(2)
        c += 1

        if c > 5:
            print()
            c = 0
# run_ballad(c)

#if you wanted their to be a line break every three lines, how would you do it?

#something like if line_count % 3 == 0 (this checks if it is divisible by 3)

def run_ballad_stanza(count):
    while count < 6:
        if count == 3:
            print()
            ballad_stanza(count)
            time.sleep(2)
        else:
            ballad_stanza(count)
            time.sleep(2)
        count += 1
        if count > 5:
            print()
            count = 0
run_ballad_stanza(c)
