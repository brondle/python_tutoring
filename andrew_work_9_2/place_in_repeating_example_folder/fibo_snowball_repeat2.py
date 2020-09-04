from fp import FP
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
# print(poem)

#def ps(fib):
#    for i in range(fib):
#        print('i: ', i)
#        if i == 0:
#            continue
#        ps.phrase = ''
#        phrase = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, i)
#        rn = int(random.random()*len(phrase)-1)
#        str_phrase = ' '.join(phrase[rn])
#        ps.phrase = ps.phrase + str_phrase+" "
#        yield ps.phrase
#        print(ps.phrase)

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

# run_ps()
#the run_ps() and ps(fib) phonetic snowball and for loop based on fibo length above works fine, just uncomment the ps(5) above
#but what they do is build an increasing snowball poem that goes back and repeats the sequence each time

#this is the yield + next, one at a time version

# NEVER DECLARE THE SAME FUNCTION TWICE
def ps(ind, arr):
    for i in range(ind):
        ps.phrase = ''
        phrase = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, arr[i])
        rn = int(random.random()*len(phrase)-1)
        str_phrase = ' '.join(phrase[rn])
        ps.phrase = ps.phrase + str_phrase+" "
        yield ps.phrase

ps.phrase = ''
#the ind argument is the number of index items before repeating
#arr is the list of items the fibonacci list

fibo_list = [1, 1, 2, 3, 5, 8]
fibo_list2 =[1, 1, 2, 3]

# while True:
#     for j in (ps(5, fibo_list)):
#         print(j)
#         time.sleep(1)
        # print()
    # the_phrases = run_ps2()

#Sept 3rd work with Brent

def ps_big(ind, arr):
    for i in range(ind):
        for j in range(i):
            ps_big.phrase = ''
            phrase = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, arr[i])
            rn = int(random.random()*len(phrase)-1)
            str_phrase = ' '.join(phrase[rn])
            ps_big.phrase = ps_big.phrase + str_phrase+" "
            yield ps_big.phrase
ps_big.phrase = ''

while True:
    for j in (ps_big(5, fibo_list)):
        print(j)
        time.sleep(1)



#
# def sequential2():
#     next(the_phrases)
#     print()
    # sequential2.count += 1
    # if sequential2.count > 20:
    #     repeat_text.stop()

# sequential2.count = 0
# repeat_text2 = repeating.Repeat(1, sequential2)
# repeat_text2.start()


#what if I save the combinations in strings or lists?
#this is the original fibo
# for i in fibo_list:
#     print('\n')
#     for j in range(i):
#         phrase = phonetic_snowball(j)
#         print(phrase)



def add_build():
    z = fibo_list
    for i in z:
        # add_build.expanding = add_build.expanding + (random.random()*5) * i
        add_build.expanding += add_build.expanding * i +1

        # add_build.expanding = v * v
        yield(add_build.expanding)

add_build.expanding = 1
rando = add_build()
def next_comp():
    print(next(rando))
    # print(add_build())
    next_comp.count +=1
    if next_comp.count > 5:
        my_repeat.stop()
next_comp.count = 0
# my_repeat = repeating.Repeat(1, next_comp)
# my_repeat.start()

# print('my gen starts here')
def yield_func():
    n = range(20)
    for i in n:
        yield i*i

gen = yield_func()
def my_gen():
    print(next(gen))
    my_gen.cntr +=1
    if my_gen.cntr >3:
        print('stopping my gen')
        rpt_my_gen.stop()

my_gen.cntr = 0
# rpt_my_gen = repeating.Repeat(1, my_gen)
# rpt_my_gen.start()

# print('the list example is below')
# Using : list()
#A list is an iterable object that has its elements inside brackets.Using list() on a generator object will give all the values the generator holds.
def even_numbers(n):
    for x in range(n):
       if (x%2==0):
           yield x

numTTT = even_numbers(20)
def one_at_a_time():
    print('we here')
    print(next(numTTT))
    one_at_a_time.count = one_at_a_time.count + 1
    print('this is the one at a time count ', one_at_a_time.count)
    if one_at_a_time.count > 5:
        print('im gonna stop now')
        r.stop()
one_at_a_time.count = 0

# r = repeating.Repeat(1, one_at_a_time)
# r.start()

#
# print("this is the next method")
this_num = yield_func()
# print(next(this_num))
# print(next(this_num))
# print(next(this_num))




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

#psdblfibo(fibo_list2)
# print(one)
# print(two)
# print(three)
# print(four)




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

