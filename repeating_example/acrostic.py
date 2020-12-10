import nltk
import random
import re
import time
prondict = nltk.corpus.cmudict.dict() #this is the important line
from nltk.tokenize import WhitespaceTokenizer, sent_tokenize, word_tokenize
f = open('artistStatements.txt') #add your text here
raw_text = f.read()
sentence = sent_tokenize(raw_text)
words = word_tokenize(raw_text)

def pick_word():
    my_choice = random.choice(words)
    return my_choice

def test_length(word):
    return len(word) > 6

def picker():
#    for i in range(len(words)):
    v = pick_word()
    print('test length: ', test_length(v))

    if test_length(v):
        return v
    else:
        return picker()

def broken_up(acrostic):
    letters = list(acrostic)
    return letters

def letter_word(l):
    temp_list = []
    for i in words:
        if i[:1] == l:
            temp_list.append(i)
    chosen_word = random.choice(temp_list)
    return chosen_word

# acrostic = picker()
# lettre = broken_up(acrostic)
# no_first_ltr = lettre[1:]
#
# print(acrostic)
# for i in no_first_ltr:
#     # print(i)
#     word_is = letter_word(i)
#     print(word_is)


def acrostic():
    acrostic = picker()
    lettre = broken_up(acrostic)
    word_is = ''
    for i in lettre[1:len(lettre)]:
        word_is = word_is + ' '+ letter_word(i)
    combo = acrostic + word_is
    collection = combo.split()
    for j in collection:
        print(j)

acrostic()
#maybe use pos in combination (like an exquisite corpse
