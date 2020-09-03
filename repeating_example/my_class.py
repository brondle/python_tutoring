from fp import FP
# import find_phoneme_oop
from fp import refactored_find_phonemes, find_phonemes_ngram
# from Find_phoneme import phoneme_list
# from find_phoneme *

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
# print(type(phonemes))

g = FP.phonemeList(num, phonemes, sentence)

# print(g[0])


z = refactored_find_phonemes(num, phonemes, sentence)
# print(z[50])

z = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, 5)
ph = FP.phonemeList_ngram(-2, ['AH0', 'N'], sentence, 3)
#
# print(z)
# print(ph)

# for i in range(5):
#     print(find_phonemes_ngram(-2, ['AH0', 'N'], sentence, i))
poem = ''
my_list = []
# print('the length of sentence is ', len(sentence))

for i in range(5):
    phrase = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, i)
    rn = int(random.random()*len(phrase)-1)
    str_phrase = ' '.join(phrase[rn])
    poem = poem + str_phrase + '\n'
print(poem)

def ps(fib):
    for i in range(fib):
        ps.phrase = ''
        phrase = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, i)
        rn = int(random.random()*len(phrase)-1)
        str_phrase = ' '.join(phrase[rn])
        ps.phrase = ps.phrase + str_phrase+" "
        print(ps.phrase)

ps.phrase = ''
# ps(5)

fibo_list = [0, 1, 1, 2, 3, 5, 8]
fibo_list2 =[0,1, 1, 2, 3]
# for i in fibo_list:
#     ps(i)
#     print()
#try running this with a yield and repeat
def run_ps():
    for i in fibo_list:
        ps(i)
        print()

#----the ps(fib) phonetic snowball and for loop based on fibo length above works fine, just uncomment the ps(5) above
#but what they do is build an increasing snowball poem that goes back and repeats the sequence each time

#what if I save the combinations in strings or lists?
#this is the original fibo
# for i in fibo_list:
#     print('\n')
#     for j in range(i):
#         phrase = phonetic_snowball(j)
#         print(phrase)

#how to quickly make a batch of lists
one, two, three, four, five, = [],[],[],[],[]

j = 0
def psdblfibo(fib):
    for i in fibo_list2:
        for j in range(0,i+1):
            print('j is ', j, 'i is ', i)
            if i == 0:
                print('i equals ', i)
                phrase = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, i)
                rn1 = int(random.random() * len(phrase) - 1)
                str_phrase = ' '.join(phrase[rn1])
                one.append(str_phrase)

            if i == 1:
                print('i equals ', i)
                phrase = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, i)
                # rn1 = int(random.random() * len(phrase) - 1)
                # str_phrase = ' '.join(phrase[rn1])
                # one.append(str_phrase)

                rn2 = int(random.random() * len(phrase) - 1)
                str_phrase2 = ' '.join(phrase[rn2])
                two.append(str_phrase2)

            if i == 2:
                print('i equals ', i)
                phrase = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, i)
                # rn2 = int(random.random() * len(phrase) - 1)
                # str_phrase2 = ' '.join(phrase[rn2])
                # two.append(str_phrase2)
                rn3 = int(random.random() * len(phrase) - 1)
                str_phrase3 = ' '.join(phrase[rn3])
                three.append(str_phrase3)

            if i == 3:
                print('i equals ', i)
                phrase = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, i)
                # rn3 = int(random.random() * len(phrase) - 1)
                # str_phrase3 = ' '.join(phrase[rn3])
                # three.append(str_phrase3)

                rn4 = int(random.random() * len(phrase) - 1)
                str_phrase4 = ' '.join(phrase[rn4])
                four.append(str_phrase4)

psdblfibo(fibo_list2)
print(one)
print(two)
print(three)
print(four)




# psdblfibo(5)

# for i in fibo_list:
#     psdblfibo(i)
#     print()

# this_phrase =''
# for i in fibo_list:
#     # print("i is ", i)
#     phrase = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, i)
#     rn = int(random.random() * len(phrase) - 1)
#     str_phrase = ' '.join(phrase[rn])
#     # print(type(str_phrase), str_phrase, type(phrase), phrase)
#     this_phrase = this_phrase + " " + str_phrase
#     print(this_phrase)

