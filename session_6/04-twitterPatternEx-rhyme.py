from __future__ import print_function
from __future__ import unicode_literals

from builtins import str, bytes, dict, int
from builtins import range

import pronouncing

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from pattern.web import Twitter, hashtags
from pattern.db import Datasheet, pprint, pd
import random
# This example retrieves tweets containing given keywords from Twitter.

try:
    # We'll store tweets in a Datasheet.
    # A Datasheet is a table of rows and columns that can be exported as a CSV-file.
    # In the first column, we'll store a unique id for each tweet.
    # We only want to add the latest tweets, i.e., those we haven't seen yet.
    # With an index on the first column we can quickly check if an id already exists.
    # The pd() function returns the parent directory of this script + any given path.
    table = Datasheet.load(pd("eulogy.csv"))
    index = set(table.columns[0])
except:
    table = Datasheet()
    index = set()

engine = Twitter(language="en")

# With Twitter.search(cached=False), a "live" request is sent to Twitter:
# we get the most recent results instead of those in the local cache.
# Keeping a local cache can also be useful (e.g., while testing)
# because a query is instant when it is executed the second time.

search_term = 'beat'
prev = None
for i in range(2):
    # print('the i is ', i)
    for tweet in engine.search(search_term, start=prev, count=25, cached=False):
        t = tweet.text
        src_str = tweet.text
        # t_list = t.split()
        print('the source text is ', src_str)
        rhymes = pronouncing.rhymes(search_term)
        rhyme_choice = random.choice(rhymes)

        str_replaced = src_str.replace(search_term, rhyme_choice )
        print('the string replace is ', str_replaced)

        # for word in t_list:
        #     print(word)
        #     if word == 'beat':
        #         print('beat is found ')
        #         rhymes = pronouncing.rhymes(word)
        #         print('rhymes ', rhymes)
        #         if len(rhymes)>0:
        #             t_list.append(random.choice(rhymes))
        #             print('the rhymed word is and the new tweet is ', t_list)

            # print('the word is ', word)
            # rhymes = pronouncing.rhymes(word)
            # if random.randrange(4) == 0 and len(rhymes) >0:
            #     t_list.append(random.choice(rhymes))
            #     print('the rhyming tweet is ', t_list )



        # print("")
        # print(tweet.text)
        # print(tweet.author)
        # print(tweet.date)
        # print(hashtags(tweet.text))  # Keywords in tweets start with a "#".
        print("")
        # Only add the tweet to the table if it doesn't already exists.
        # if len(table) == 0 or tweet.id not in index:
        #     table.append([tweet.id, tweet.text])
        #     index.add(tweet.id)
        # Continue mining older tweets in next iteration.
        # prev = tweet.id

# Create a .csv in pattern/examples/01-web/
# table.save(pd("eulogy_july_21.csv"))

# print("Total results: %s" % len(table))
# print("")

# Print all the rows in the table.
# Since it is stored as a CSV-file it grows comfortably each time the script runs.
# We can also open the table later on: in other scripts, for further analysis, ...

# print(table, truncate=100)

# Note: you can also search tweets by author:
# Twitter().search("from:tom_de_smedt")
