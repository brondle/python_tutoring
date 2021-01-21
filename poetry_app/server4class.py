from flask import Flask, render_template
import random
import sys
import nltk
import time

from nltk.tokenize import WhitespaceTokenizer, sent_tokenize
from helpers.fp import find_phonemes_ngram

#to see the results of your program, run this file, then go to the localhost:5000/name_of_app
#the name_of_app is what follows the @app.route('/phonetic_snow'), in this case it would be localhost:5000/phonetic_snow

prondict = nltk.corpus.cmudict.dict()
# f = open('artistStatements.txt') #your text goes here
f = open('languageofnewmedia.txt') #your text goes here
raw2 = f.read()
sentence = sent_tokenize(raw2)

app = Flask(__name__)

def ps_simple(lines):
    ps_simple.phrase = ''
    for i in range(lines):
        phrase = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, i)
        rn = int(random.random()*len(phrase)-1)
        str_phrase = ' '.join(phrase[rn])
        ps_simple.phrase = ps_simple.phrase + str_phrase+" "+'<br/>'
        yield ps_simple.phrase
ps_simple.phrase = ''

def run_simple():
    x = next(run_simple.x, 'end')
    if (x) == 'end':
        run_simple.x = ps_simple(5)
        return next(run_simple.x)
    else:
        return x

run_simple.x = ps_simple(5)

@app.route('/phonetic_snow')
def fibo_phone():
    my_variable = run_simple()
    return render_template("button_refresh.html", words=my_variable)

if __name__ == '__main__':
  app.run()