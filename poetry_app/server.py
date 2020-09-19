from flask import Flask, render_template
import random
import sys
import nltk
import time
import fp
# from fp import r_punct_list
# from rhymes import find_alliteration, find_phonemes, gen_rhyme_pair
from helpers.rhymes import find_alliteration, find_phonemes, gen_rhyme_pair, gen_rando, gen_one_phone
from helpers.this_helper import gen_random_num
from nltk.tokenize import WhitespaceTokenizer, sent_tokenize
from helpers.fp import find_phonemes_ngram
# sys.path.append('/Users/ademirji/PycharmProjects/NaturalLangage/Tuesdays/python_tutoring/poetry_app/helpers/')
# h_dir = '/Users/ademirji/PycharmProjects/NaturalLangage/Tuesdays/python_tutoring/poetry_app/helpers'
# h_dir ='./helpers'
# sys.path.append('h_dir')

#to run this program, cd into the directory then start/run the program. then go to the localhost:5000/name_of_app

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
# print(allit_list)
s = ' '
for i in range(len(allit_list)):
    n = int(random.random()*len(allit_list))
    my_phrase = allit_list[n]
    s = ' '.join(my_phrase)
# print(s)
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
    # return str(gen_rando())
    # return str(" ".join(b))
   greeting = random.choice(greets) + ", " + random.choice(places)
   return render_template("greetings.html",
     greet=random.choice(greets), place=random.choice(places))


@app.route('/allit')
def allit():
    for i in range(len(allit_list)):
        n = int(random.random() * len(allit_list))
        my_phrase = allit_list[n]
        s = ''.join(my_phrase)
        # print(s)
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
        # print(s)
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
fibo_list2 =[0,1, 1, 2, 3, 5]
new_list = [1, 1, 2, 3, 5, 8]

def ps_simple(fib):
    ps_simple.phrase = ''
    for i in range(fib):

        phrase = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, i)
        rn = int(random.random()*len(phrase)-1)
        str_phrase = ' '.join(phrase[rn])
        ps_simple.phrase = ps_simple.phrase + str_phrase+" "+'<br/>'
        # print(ps.phrase)
        yield ps_simple.phrase
ps_simple.phrase = ''
# ps(5)

def run_simple():
    # print(run_simple.x)
    x = next(run_simple.x, 'end')
    if (x) == 'end':
        run_simple.x = ps_simple(5)
        return next(run_simple.x)
    else:
        return x

run_simple.x = ps_simple(5)

@app.route('/fibo_phone')
def fibo_phone():
    my_variable = run_simple()
    return render_template("simple.html", words =my_variable)

def ps(fib):
    for i in range(len(fib)):
        ps.phrase = ''
        phrase = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, i)
        rn = int(random.random()*len(phrase)-1)
        str_phrase = ' '.join(phrase[rn])
        ps.phrase = ps.phrase + str_phrase+" "
    for i in fib:
        dur = 1
        if i > 2:
            dur = 4
        elif i > 3:
            dur = 5
        else:
            dur = 1
        time.sleep(dur)
        print()
        for j in range(i):
            ps.phrase = ''
            phrase = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, i-1)
            rn = int(random.random()*len(phrase)-1)
            # no_punct_phrase = r_punct_list(phrase[rn])
            str_phrase = ' '.join(phrase[rn])
            # str_phrase = ' '.join(no_punct_phrase)
            ps.phrase = ps.phrase + str_phrase+" "
            # print(ps.phrase)
            return ps.phrase
ps.phrase = ''

def run_ps():
    # for i in fibo_list:
    #     ps(i)
    #     print()
    #if we want to loop it N times
    for i in range(3):
        neo = ps(fibo_list2)
        # print('this is the run_ps four second pause')
        # time.sleep(4)
        return neo

@app.route('/fibo_phone2')
def fibo_phone2():
    # my_variable = ps(5)
    my_variable2 = run_ps()
    # for i in range(3):
    #     my_variable = ps_simple(5)
    #     time.sleep(2)
    return render_template("simple.html", words =my_variable2)


if __name__ == '__main__':
  app.run()




#to run this code, cd into the location where the file is and then goto your browser: localhost:5000/hello
