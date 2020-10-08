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

f = open('artistStatements.txt')
raw2 = f.read()
sentence = sent_tokenize(raw2)
num = -2
phon_a = ['AH0', 'N']
phon_b = ['AH0', 'L']
phon_c = ['AW1', 'ER0']

rain = 'the rain in spain falls mainly on the plain'
rain_list = rain.split()
erase_list = []

def seq_of_sents(sentence, num_of_sents):
    dont_exceed = len(sentence)-num_of_sents
    r_choice = random.randint(0, dont_exceed)
    return sentence[r_choice:r_choice+(num_of_sents)]

num = 20
#randomly pick n sentences
this_choice = seq_of_sents(sentence,num)

def erase_words(word_list, all_but_n):
    sent_length = len(word_list)
    num_to_erase = sent_length - all_but_n
    erase_list = random.sample(word_list, num_to_erase)
    # print(sent_length,num_to_erase,'\n', erase_list)
    for i in range(len(word_list)):
        if word_list[i] in erase_list:
            char_length = len(word_list[i])
            em = ' '
            word_list[i] = em*char_length
        else:
            word_list[i] = word_list[i]
            # print(word_list[i])
    erased_string = list_to_str(word_list)
    return erased_string

def list_to_str(input_seq):
   # Join all the strings in list
   final_str = ' '.join(input_seq)
   return final_str

print('\n'*2)
# for i in range(len(this_choice)):
#     new_erase_list = this_choice[i].split()
#     rn = random.randint(1,5)
#     print(erase_words(new_erase_list,rn))


def erase_sentence(list_of_strings):
    for i in range(len(list_of_strings)):
        new_erase_list = list_of_strings[i].split()
        rn = random.randint(1, 5)
        erasure = erase_words(new_erase_list, rn)
        print(erase_words(new_erase_list, rn))
    # return erasure


print(erase_sentence(this_choice))
