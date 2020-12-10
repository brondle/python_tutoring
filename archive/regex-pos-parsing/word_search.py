from __future__ import print_function
import nltk
from nltk.tokenize import WhitespaceTokenizer, sent_tokenize
# import random
from random import choice, randint
from nltk.tokenize import WhitespaceTokenizer, sent_tokenize, word_tokenize
from itertools import permutations
import time, os, sys, sched
import repeating, string
from textblob import TextBlob
from textblob import Word
from nltk.stem import WordNetLemmatizer
import helper
from nltk.corpus import wordnet as wn # allows us to access pos types
#help(nltk.corpus.reader)
from nltk.corpus import PlaintextCorpusReader
# corpus_root = '/usr/share/dict'
# corpus_root = '/Users/ademirji/PycharmProjects/NaturalLangage/texts'
# corpus_root = './'
# corpus = PlaintextCorpusReader(corpus_root, '.*')
# reggy = nltk.Text(corpus.words('artistsStatements.txt'))
z = nltk.corpus.gutenberg.fileids()
f = open('artistStatements.txt')

# use the decode method to convert to ascii (textblob prefers ascii)
# raw = sys.stdin.read().decode('ascii', errors="replace")
raw = f.read()
rawShort = raw[:400]
raw_split = raw.split()
f.close()
artBlob = TextBlob(raw)
shrtBlob = TextBlob(rawShort)
aBLength = len(artBlob)
wList = artBlob.words
posShort = shrtBlob.tags
tags = artBlob.tags
noun_phrases = artBlob.noun_phrases
ccS = shrtBlob.sentences

print(rawShort)
print(type(rawShort), type(raw_split))
print(type(artBlob))

search_term = 'the'
s_they, s_the, s_we = 'they', 'the', 'we'
s_i = 'I'
the_plus = []
they_plus = []
i_plus = []
we_plus_three = []

print(raw_split[:40])


for w in range(len(raw_split)-1):
    if raw_split[w] == s_the:
        temp1 = raw_split[w] + " " + raw_split[w +1]
        the_plus.append(temp1)
    if raw_split[w] == s_they:
        temp2 = raw_split[w] + " " + raw_split[w+1]
        they_plus.append(temp2)
    if raw_split[w] == s_i:
        temp3 = raw_split[w] + " " + raw_split[w+1]
        i_plus.append(temp3)
for i in range(len(raw_split)-3):
    if raw_split[i] == s_we:
        temp4 = raw_split[i] + " " + raw_split[i+3]
        we_plus_three.append(temp4)





print('the ', len(the_plus), 'they ', len(they_plus), 'i ', len(i_plus), 'we ', len(we_plus_three))
print(the_plus)
print(they_plus)
print(i_plus)
print(we_plus_three)


for i, items in enumerate(posShort):
    print(i, items, items[0], items[1])

# for i, items in enumerate(ccS):
#     posCCS = ccS.tags
#     if items[1] == 'CC':
#         print(i, items[0])


adjNounCombo, verbAdverb, aVerb, aPlNoun, adj, gerund, noun, determiner, lngCmbo = [], [],[], [],[], [], [], [], []

def removePunctuation(text):
    text = text.lower()
    exclude = set(string.punctuation)
    keep_these_punct = ['/', '%', '-']
    for punct in keep_these_punct:
        exclude.remove(punct)
    converted_text = ''.join(ch for ch in text if ch not in exclude)
    return converted_text

for i, items in enumerate(tags):
    if items[1] == 'JJ' and tags[i+1][1] == 'NN':
        theCombo = (items[0], tags[i+1][0])
        thisCombo = " ".join(theCombo)
        adjNounCombo.append(thisCombo)
        # print(items[0], tags[i+1][0])
        # print(items, tags[i+1])
# print(adjNounCombo)

for i, items in enumerate(tags):
    if items[1] == 'VBD' and tags[i+1][1] == 'RB':
        theCombo2 = (items[0], tags[i+1][0])
        thisCombo2 = " ".join(theCombo2)
        verbAdverb.append(thisCombo2)
        # print(items[0], tags[i+1][0])
        # print(items, tags[i+1])
# print(verbAdverb)

for i, items in enumerate(tags):
    if items[1] == 'JJ' and tags[i+1] == 'JJ' and tags[i+2] == 'JJ' and tags[i+3] =='CC' and tags[i+4] =='JJ' and tags[i+5]=='NNS':
        myLongCombo = (items[0], tags[i+1][0], tags[i+2][0], tags[i+3][0], tags[i+4][0], tags[i+5][0])
        myLongCombo = " ".join(myLongCombo)
        lngCmbo.append((myLongCombo))


print(lngCmbo)
for i, items in enumerate(tags):
    if items[1] == 'VB':
        aVerb.append(items[0])

for i, items in enumerate(tags):
    if items[1] == 'NNS':
        aPlNoun.append(items[0])

for i, items in enumerate(tags):
    if items[1] == 'JJ':
        adj.append(items[0])

for i, items in enumerate(tags):
    if items[1] == 'NN':
        noun.append(items[0])

for i, items in enumerate(tags):
    if items[1] == 'VBG':
        gerund.append(items[0])

for i, items in enumerate(tags):
    if items[1] == 'DT':
        determiner.append(items[0])



#outputRange
oR = 1
for i in range(oR):
    print(choice(adjNounCombo) +','+ " " +choice(verbAdverb), choice(noun_phrases))
print('\n')
for i in range(oR):
    print(choice(noun_phrases), choice(aVerb), choice(noun_phrases))
print('\n')
for i in range(oR):
    print(choice(aPlNoun), choice(aVerb), choice(noun_phrases))
print('\n')
for i in range(oR):
    print(choice(aPlNoun), choice(aVerb), choice(adj))
print('\n')
for i in range(oR):
    print(choice(aPlNoun), choice(aVerb), choice(adjNounCombo))
#this is a pattern from videogrep
print('\n')
for i in range(oR):
    print(choice(gerund), choice(determiner), choice(adjNounCombo))
print('\n')



count = 0
def rptGerundPat():
    global count
    print(choice(gerund), choice(determiner), choice(adjNounCombo))
    count = count + 1
    # print(count)
    if count > 10:
        r.stop()
    return count

r = repeating.Repeat(2, rptGerundPat)
#to turn on uncomment the start
# r.start()

#this is the example from allison parrish, it creates a recipe
#modify this to mimick the 'At Home' language in the NYTimes, or something to create spells - maybe collaborate with Sarah Potter
# verbs = list()
# for word, tag in artBlob.tags:
#     if tag == 'VB':
#         verbs.append(word.lemmatize())
#
# for i in range(1, 11):
#     print("Step " + str(i) + ". " + choice(verbs).title() + " " + choice(noun_phrases))

#this is an ex. of creating a bag of nouns and adjectives to mix them randomly (without ennumerate
# nouns = list()
# adjectives = list()
# for word, tag in artBlob.tags:
#     if tag == 'NN' or tag == 'NNS':
#         nouns.append(word.lemmatize())
#     if tag == 'JJ' or tag == 'JJR' or tag == 'JJS':
#         adjectives.append(word.lemmatize())
#
# for i in range(10):
#     print(choice(adjectives), choice(nouns))

#Apply lemmatization to words in a list
# def lemmatizeWords(words):
#     convert_words = []
#     words_with_pos = nltk.pos_tag(words)
#     for pos_tag in words_with_pos:
#         simplify_pos = penn_to_wn(pos_tag[1])
#         if(simplify_pos == None):
#             convert_words.append(wordnet_lemmatizer.lemmatize(pos_tag[0]))
#         else:
#             convert_words.append(wordnet_lemmatizer.lemmatize(pos_tag[0], simplify_pos))
#     #print(words == convert_words)
#     return convert_words



def rPunct(text):
    return [word.lower() for word in text if word.isalpha()]

w = string
myNewList = []

#the key difference between these is that isalpha will remove the string
def myConversionPunct(text):
    word = text.lower()
    word = word.split()
    for w in word:
        if w.isalpha():
            myNewList.append(w)
            # print(w)
    convert = " ".join(myNewList)
    return(convert)





u = Word("rocks")
w = Word("better")
lemTest = Word("sentences")
myString = "These sentences doesn't have much of a point, it is mostly an example. 'The thing is', he said, 'I suffer from painful rectal itch.'"
myS = Word(myString)
# myString = myString.lower()
# print(rPunct(myString))
# print(myConversionPunct(myString))
# print(removePunctuation(myString))
# print("rocks :", u.lemmatize())
# print("better : ", w.lemmatize("a"))
# print(myS.lemmatize())
# print(lemTest.lemmatize())

mySplitString = myString.split()
tempList = []

for i in mySplitString:
    newLem = Word(i)
    z = newLem.lemmatize()
    print(z)
    tempList.append(z)

print(" ".join(tempList))


