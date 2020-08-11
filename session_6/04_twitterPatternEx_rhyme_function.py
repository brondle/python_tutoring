from __future__ import print_function
from __future__ import unicode_literals

from builtins import str, bytes, dict, int
from builtins import range
import repeating
import pronouncing

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from pattern.web import Twitter, hashtags
from pattern.db import Datasheet, pprint, pd
import random
# This example retrieves tweets containing given keywords from Twitter.

engine = Twitter(language="en")
prev = None

word = 'beat'
tweet_index = []

def send_text():
    print(search_replace(word))

def search_replace(word):
    search_term = word
    for i in range(10):
        for tweet in engine.search(search_term, start=prev, count=1, cached=False):
            if tweet.id not in tweet_index:
                tweet_index.append(tweet.id)
                # global count
                t = tweet.text
                src_str = tweet.text
                rhymes = pronouncing.rhymes(search_term)
                rhyme_choice = random.choice(rhymes)
                str_replaced = src_str.replace(search_term, rhyme_choice)
                formatted = src_str + '\n' + str_replaced

                if len(tweet_index)>4:
                    r.stop()

                return formatted



# print(search_replace('beat'))

r = repeating.Repeat(8, send_text)
r.start()