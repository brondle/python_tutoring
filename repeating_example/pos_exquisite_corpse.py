import nltk
import re,time
from random import randint
f = open('artistStatements.txt') #put your text here
raw = f.read()
f.close()
sentence = nltk.sent_tokenize(raw)
#article + adjective + noun + verb (or verb modifier and verb) + article + adjective + noun
#The exquisite corpse shall drink the new wine

#this is the simple version of the pos tagger
sent = 'a wide array of sugar and proteins make up any American diet'
s = nltk.word_tokenize(sent)
# print('this is the sentence ', s)
tagged = nltk.pos_tag(s)
# print(tagged)

#this shows how to tokenize and tag a sentence from a text file like a novel
word_toke = nltk.word_tokenize(sentence[0])#the [0] here means, use the first sentence
tg2 = nltk.pos_tag(word_toke)
# print('this is tg2', tg2)

#this separates all the language in the file into a list of one word or token (like commas, periods, etc..)
art_blob = nltk.word_tokenize(raw)
#make an empty list for the parts of speech (pos) you want, I made up these variable names
art_list, v_list, adj_list, n_list, adv_verb = [],[],[],[],[]
#if you want to use multiple types of pos for a search you can also make a variable that combines two, see them used in line 43 (the make_lists code)
nouns = 'NN' or 'NNP'
adverbs = 'RB' or 'RBS' or 'RBR'

#this shows you how to create a series of functions that work together to tag a text file, then generate an exquisite corpse form
def remove_punctuation(w):
    word = re.sub(r'[^\w\s]', '', w.lower())
    return word

def pos_tagger(text, pos, pos_list):
    for (word, tag) in nltk.pos_tag(text):
        if tag == pos:
            if word not in pos_list:
                pos_list.append(word)
    return pos_list

def make_lists():
    pos_tagger(art_blob, 'DT', art_list),pos_tagger(art_blob, "RB", adv_verb),pos_tagger(art_blob, 'JJ', adj_list),pos_tagger(art_blob, nouns, n_list), pos_tagger(art_blob, 'VBZ', v_list)

def r(list_of_words):
    n = len(list_of_words)-1
    r = randint(0, n)
    chosen = list_of_words[r]
    chosen = remove_punctuation(chosen)
    return chosen

make_lists() #call the make_lists function to get the lists ready
print('\n'*3)#put some blank space above the output

def gen_exquisite():
    print(r(art_list), r(adj_list), r(n_list),r(v_list), r(art_list), r(adj_list), r(n_list))
    # print("The", r(adj_list), r(n_list), r(v_list), 'a', r(adj_list), r(n_list))

#print one exquisite corpse
gen_exquisite()

#print 1000 lines of text (change the variable in the for loop to however many you'd like
# for i in range(100):
#     gen_exquisite()
#     print()

#continually output a new exquisite corpse line every two seconds
# while True:
#     gen_exquisite()
#     print()
#     time.sleep(2)



