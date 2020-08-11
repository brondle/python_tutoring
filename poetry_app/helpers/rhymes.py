import nltk
import random
from nltk.tokenize import WhitespaceTokenizer, sent_tokenize
import re
prondict = nltk.corpus.cmudict.dict()

#the goal of this program is to make a list of all words that match that last two phonemes and the three prior words
def find_phonemes(num, ph_list, sentences, outputlist):
    for i in range(len(sentences)): #could these first two lines be written like list comprehensions
        this_s = sentences[i].split()
        for j in range(len(this_s)):
            word = re.sub(r'[^\w\s]', '', this_s[j].lower())
            # print(word)
            if word in prondict and word.isalpha():
                syllable = prondict[word]
                # print(syllable)
                pho = syllable[-1][num:]
                # print(type(syllable), syllable, ' the pho is ', pho)
                if len(pho) > 1 and pho == ph_list and j-num>0 and len(word)>3:
                    location = j
                    phrase = this_s[location - 3], this_s[location - 2], this_s[location - 1], word
                    outputlist.append(phrase)
    return outputlist

def gen_rhyme_pair(rhyme_list):
    r1 = random.randint(0, len(rhyme_list)-1)
    r2 = random.randint(0, len(rhyme_list)-1)
    if r1 == r2:
        r2 = random.randint(0, len(rhyme_list)-1)
    n1 = ' '.join(rhyme_list[r1])
    n2 = ' '.join(rhyme_list[r2])
    return (n1 + '\n' + n2)


phoneBeg = 1
phoneBeg2 = 2
matchPh = ['DH', 'AH0']
# allit_list = []
def find_alliteration(sentence, outputlist):
    for i in range(len(sentence)):
        this_s = sentence[i].split()
        for j in range(len(this_s)-1):
            word = re.sub(r'[^\w\s]', '', this_s[j].lower())
            word2 = re.sub(r'[^\w\s]', '', this_s[j+1].lower())
            # print(word, word2)
            if word in prondict and word.isalpha() and word2 in prondict and word2.isalpha():
                syllable = prondict[word]
                syllable2 = prondict[word2]
                # print(syllable)
                # print(syllable2)
                pho = syllable[-1][:phoneBeg2]
                next_pho = syllable2[-1][:phoneBeg2]
                # print(pho, next_pho)

                # print(word, syllable, ' the pho is ', pho, word2, syllable2, 'the next pho is ', next_pho)
                # finds alliteration for words greater than three letters long
                if pho == next_pho and len(word)>3 and len(word2)>3:
                    location = j
                    a_phrase = word, word2
                    print(word, word2)
                    outputlist.append(a_phrase)
    return outputlist

#choose a pair and convert it from a tuple to string
# my_tuple = gen_rhyme_pair()
# my1 = ' '.join(my_tuple[0])
# my2 = ' '.join(my_tuple[1])
# print(my1)
# print(my2)