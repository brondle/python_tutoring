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


rain = 'the rain in spain falls mainly on the plain'
rain_list = rain.split()

new_replace = rain
em = '     '
z = new_replace.replace('spain', em)
print(z)
#str.replace(old, new[, max])

for i in range(len(rain_list)):
    if i % 2 == 0:
        char_length = len(rain_list[i])
        em = ' '
        rain_list[i] = rain_list[i].replace(rain_list[i], em*char_length )

final_string = ' '.join(rain_list)
print('this is the final string ', final_string)
print(rain_list)

new_string = 'this is my new string, it isnt long or short or flat or thin, it is just right'
new_s_list = new_string.split()
#sampling = random.choices(list, k=4)
# r_choice = random.choice(new_s_list)
# r_sample = random.sample(new_s_list, 3)
# print(r_choice, r_sample)
# print(type(new_s_list), len(new_s_list))

def list_to_str(input_seq):
   # Join all the strings in list
   final_str = ' '.join(input_seq)
   return final_str

def random_l(length, rn):
    r_list = []
    for i in range(rn):
        r_list.append(random.randint(0,length))
        return r_list
print('in the random_l funciton', random_l(18, 7))


def random_erase_replace(str_list):
    random_list = []
    new_list = []
    list_length = len(str_list)
    # r_choice = random.randint(0, list_length)
    # rn = random.randint(round(list_length/4), round(list_length/2))
    rn = random.randint(4, 8)
    print('the rn is ', rn)
    print(list_length, rn)
    random_list = random_l(list_length, rn)
    print(list_length, rn, random_list)

    for i in range(list_length):
        print('we are in the loop', i )
        # if i == r_choice:
        if i in random_list:
            char_length = len(str_list[i])
            print(i, str_list[i], char_length)
            em = ' '
            str_list[i] = str_list[i].replace(str_list[i], em*char_length)
        else:
            str_list[i] = str_list[i]

    # new_list.append(str_list[i])
    erased_string = list_to_str(str_list)
    return erased_string

print(random_erase_replace(new_s_list))
print(new_string)


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
    print(sent_length,num_to_erase,'\n', erase_list)
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



print('\n'*2)



def erase_sentence(list_of_strings):
    for i in range(len(list_of_strings)):
        new_erase_list = list_of_strings[i].split()
        rn = random.randint(1, 5)
        erasure = erase_words(new_erase_list, rn)
        print(erase_words(new_erase_list, rn))
    # return erasure


# print(erase_sentence(this_choice))