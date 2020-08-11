from flask import Flask, render_template
import random
import sys
import nltk
# from rhymes import find_alliteration, find_phonemes, gen_rhyme_pair
from helpers.rhymes import find_alliteration, find_phonemes, gen_rhyme_pair
from helpers.this_helper import gen_random_num
from nltk.tokenize import WhitespaceTokenizer, sent_tokenize
# sys.path.insert(1, '/Users/ademirji/PycharmProjects/NaturalLangage/Tuesdays/python_tutoring/poetry_app/helpers/basic')
# h_dir = '/Users/ademirji/PycharmProjects/NaturalLangage/Tuesdays/python_tutoring/poetry_app/helpers'
h_dir ='./helpers'
sys.path.append('h_dir')

z = nltk.corpus.gutenberg.fileids()
prondict = nltk.corpus.cmudict.dict()
f = open('artistStatements.txt')
raw2 = f.read()
sentence = sent_tokenize(raw2)

phoneNum = -2
phonemes = ['AH0', 'N']
scrubbed = ''
rhyme_list = []
allit_list = []
a = find_phonemes(phoneNum, phonemes, sentence, rhyme_list)
b = find_alliteration(sentence, allit_list)
print(a[0])
print(gen_rhyme_pair(rhyme_list))
print('the alliteration list is ', allit_list)
print(gen_random_num())

#
# app = Flask(__name__)
#
#
#
#
#
# if __name__ == '__main__':
#   app.run()
#



#to run this code, cd into the location where the file is and then goto your browser: localhost:5000/hello