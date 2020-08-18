from __future__ import print_function
from __future__ import unicode_literals
from flask import Flask, request
from builtins import str, bytes, dict, int
from builtins import range
import repeating
import pronouncing
from pattern.web import Twitter, hashtags
from pattern.db import Datasheet, pprint, pd
import random
import os
import sys
<<<<<<< HEAD
=======
import requests

>>>>>>> af6d442a1107190e4c7cfcdde773c6714dbe5ce0
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

engine = Twitter(language="en")
prev = None

word = 'beat'
count = 0
tweet_index = []

# def send_text():
#     print(search_replace(word))

app = Flask(__name__)

@app.route('/rhyme')
def define():
    word_str = request.args['word']
<<<<<<< HEAD
=======
    print(word_str)
>>>>>>> af6d442a1107190e4c7cfcdde773c6714dbe5ce0
    if len(word_str) == 0:
        return "no word specified!\n"
    else:
        rhymes = pronouncing.rhymes(word_str.lower())
<<<<<<< HEAD
=======
        print(rhymes)
>>>>>>> af6d442a1107190e4c7cfcdde773c6714dbe5ce0
        if len(rhymes) > 0:
            for i in range(10):
                for tweet in engine.search(rhymes, start=prev, count=1, cached=False):
                    if tweet.id not in tweet_index:
                        tweet_index.append(tweet.id)
                        global count
                        t = tweet.text
                        src_str = tweet.text
                        # rhymes = pronouncing.rhymes(word_str.lower())
                        rhyme_choice = random.choice(rhymes)
                        str_replaced = src_str.replace(word_str, rhyme_choice)
                        formatted = src_str + '\n' + str_replaced
<<<<<<< HEAD

                        if count > 4:
                            r.stop()
                        count += 1
=======
                        #
                        # if count > 4:
                        #     r.stop()
                        # count += 1
>>>>>>> af6d442a1107190e4c7cfcdde773c6714dbe5ce0
                        return formatted
        else:
            return "no rhymes found :(\n"


if __name__ == '__main__':
    app.run(debug=False)

<<<<<<< HEAD
=======
# print(requests.get('http://localhost:5000/rhyme', params={'word': '"cat"'}))

# print(requests.get('http://localhost:5000/rhyme', params={'word': '"cat"'}).content)

# r = repeating.Repeat(8, ) 
# r = repeating.Repeat(8, requests.get('http://localhost:5000/rhyme', params={'word': 'cat'})) 
# r.start()
>>>>>>> af6d442a1107190e4c7cfcdde773c6714dbe5ce0

#http://localhost:5000/rhyme?word=x, replacing x with a word of your choice.
# print(search_replace('beat'))

<<<<<<< HEAD
r = repeating.Repeat(8, define)
r.start()
=======
# r = repeating.Repeat(8, define)
# r.start()
>>>>>>> af6d442a1107190e4c7cfcdde773c6714dbe5ce0


# def search_replace(word):
#     search_term = word
#     for i in range(10):
#         for tweet in engine.search(search_term, start=prev, count=1, cached=False):
#             if tweet.id not in tweet_index:
#                 tweet_index.append(tweet.id)
#                 global count
#                 t = tweet.text
#                 src_str = tweet.text
#                 rhymes = pronouncing.rhymes(search_term)
#                 rhyme_choice = random.choice(rhymes)
#                 str_replaced = src_str.replace(search_term, rhyme_choice)
#
#                 formatted = src_str + '\n' + str_replaced
#
#                 if count > 4:
#                     r.stop()
#                 count += 1
<<<<<<< HEAD
#                 return formatted





=======
#                 return formatted
>>>>>>> af6d442a1107190e4c7cfcdde773c6714dbe5ce0
