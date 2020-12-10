from fp import FP
from fp import r_punct_list
# import find_phoneme_oop
from fp import refactored_find_phonemes, find_phonemes_ngram
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

rain = 'the rain in spain falls mainly on the plain'
rain_list = rain.split()
new_string = 'this is my new string, it isnt long or short or flat or thin, it is just right'
new_s_list = new_string.split()
new_string = 'this is my new string, it isnt long or short or flat or thin, it is just right'
new_s_list = new_string.split()

def seq_of_sents(sentence, num_of_sents):
    dont_exceed = len(sentence)-num_of_sents
    r_choice = random.randint(0, dont_exceed)
    return sentence[r_choice:r_choice+(num_of_sents)]

num = 20
#randomly pick n sentences
this_choice = seq_of_sents(sentence,num)

def list_to_str(input_seq):
   # Join all the strings in list
   final_str = ' '.join(input_seq)
   return final_str

def random_l(length, rn):
    num = random.sample(range(length), rn)
    return num

def erase_words(word_list):
    sent_length = len(word_list)
    # num_to_erase = sent_length - all_but_n
    min = round(sent_length / 2)
    max = round(sent_length / 1.20)
    rn = random.randint(min, max)
    random_list = random_l(sent_length, rn)
    # erase_list = random.sample(word_list, num_to_erase)
    # print(sent_length,num_to_erase,'\n', erase_list)
    for i in range(sent_length):
        if i in random_list:
            char_length = len(word_list[i])
            em = ' '
            word_list[i] = em*char_length

    erased_string = list_to_str(word_list)
    return erased_string

# print(erase_words(new_s_list))
# print(new_string)

limit = 7
def erase_sentence(list_of_strings):
    for i in range(len(list_of_strings)):
        new_erase_list = list_of_strings[i].split()
        # print(len(new_erase_list))
        if len(new_erase_list) > limit:
            new_erase_list= new_erase_list[:limit]
            # print(new_erase_list)
        erasure = erase_words(new_erase_list)
        ran = random.random()
        if ran > .5:
            print()
        print(erasure)
    # return erasure


# print(erase_sentence(this_choice))
erase_sentence(this_choice)
