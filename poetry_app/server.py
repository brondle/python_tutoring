from flask import Flask, render_template
import random
import sys
import nltk
# from rhymes import find_alliteration, find_phonemes, gen_rhyme_pair
from helpers.rhymes import find_alliteration, find_phonemes, gen_rhyme_pair, gen_rando, gen_one_phone, convert_lowercase
from helpers.this_helper import gen_random_num
from nltk.tokenize import WhitespaceTokenizer, sent_tokenize
# sys.path.append('/Users/ademirji/PycharmProjects/NaturalLangage/Tuesdays/python_tutoring/poetry_app/helpers/')
# h_dir = '/Users/ademirji/PycharmProjects/NaturalLangage/Tuesdays/python_tutoring/poetry_app/helpers'
# h_dir ='./helpers'
# sys.path.append('h_dir')

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
one_phone = gen_one_phone(rhyme_list)
find_alliteration(sentence, allit_list)
print(allit_list)
s = ' '
for i in range(len(allit_list)):
    n = int(random.random()*len(allit_list))
    my_phrase = allit_list[n]
    s = ' '.join(my_phrase)
print(s)
# print(a[0])
# print(gen_rhyme_pair(rhyme_list))
# print(gen_random_num())
greets = ["Hello", "Hi", "Salutations", "Greetings", "Hey", "Sup"]
places = ["region", "continent", "world", "solar system",
  "galaxy"]

app = Flask(__name__)
greets = ["Hello", "Hi", "Salutations", "Greetings", "Hey", "Sup"]
places = ["region", "continent", "world", "solar system",
  "galaxy"]

@app.route('/hello')
def hello():
    return str(gen_rando())
  # greeting = random.choice(greets) + ", " + random.choice(places)
  # return str(" ".join(b))
  # return render_template("greetings.html",
  #   greet=random.choice(greets), place=random.choice(places))
@app.route('/allit')
def allit():
    for i in range(len(allit_list)):
        n = int(random.random() * len(allit_list))
        my_phrase = allit_list[n]
        s = ''.join(my_phrase)
        print(s)
    return s

@app.route('/test1')
def test1():
    greeting = random.choice(greets) + ", " + random.choice(places)
    return render_template("greetings.html",
    greet=random.choice(greets), place=random.choice(places))

@app.route('/test2')
def test2():
    for i in range(len(allit_list)):
        n = int(random.random() * len(allit_list))
        my_phrase = allit_list[n]
        s = ''.join(my_phrase)
        print(s)
    # greeting = random.choice(greets) + ", " + random.choice(places)
    return render_template("simple.html",
                           words=s)

my_string = 'this is going to be the best day of my life'
@app.route('/best')
def print_to_web():
    return render_template("simple.html",words =my_string )

@app.route('/phone')
def phone():
    this_phone = gen_one_phone(rhyme_list)
    return render_template("simple.html", words =this_phone)
#not sure why text is centered in the html

fibo_list = [0, 1, 1, 2, 3, 5, 8]

def fibo_series():
#    phr = gen_one_phone(rhyme_list)
    phr = 'AAAAA'
    convert_lowercase(phr)
    print('phr: ', phr)
    phr = convert_lowercase(phr)
    print('phr: ', phr)
    # rp = remove_punctuation(phr)
    # convert_lowercase(rp)
    print(phr)
print('fibo series: ', fibo_series())

def getFibonnaciSeries(num):
    c1, c2 = 0, 1
    count = 0
    while count < num:
        yield c1
        c3 = c1 + c2
        c1 = c2
        c2 = c3
        count += 1

fin = getFibonnaciSeries(7)

def run_fibo():
    for i in fin:
        print('\n')
        for j in range(i):
            phrase = fibo_series()

@app.route('/fibo')
def fibo():
    for i in fin:
        print('\n')
        for j in range(i):
            phrase = fibo_series()
    # my_poem = run_fibo()
    return render_template('simple.html', words=phrase)

if __name__ == '__main__':
  app.run()




#to run this code, cd into the location where the file is and then goto your browser: localhost:5000/hello
