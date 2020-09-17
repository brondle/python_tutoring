import nltk
import random
from nltk.tokenize import WhitespaceTokenizer, sent_tokenize
import re
prondict = nltk.corpus.cmudict.dict()

from nltk.tokenize import WhitespaceTokenizer, sent_tokenize
z = nltk.corpus.gutenberg.fileids()
f = open('artistStatements.txt')
raw2 = f.read()
sentence = sent_tokenize(raw2)

phonemes = ['AH0', 'N']
# print(type(phonemes))

def refactored_find_phonemes(num, ph_list, sentences):
    #if outputlist is, presumably, an empty list, there's no reason to include it in the declaration
    output = []
    #same thing with range - if we're just using array[i], it's simpler to just use for in on the array itself
    for i in sentences:
        sent = i.split()
        for j in range(len(sent)):
            word = re.sub(r'[^\w\s]', '', sent[j].lower())
            #why are we checking "isalpha?"
            if word in prondict:
                syl = prondict[word]
                pho = syl[-1][num:]
                location = j
                phrase = sent[location-3:location+1]
                # if pho == ph_list then it's definitely longer than 1, so we don't need to check that
                if pho == ph_list and len(word)>3 and len(phrase)>0:
                    # print('pho: ', pho)
                    # print('phrase: ', phrase)
                    output.append(phrase)
    return output


# this_phone = refactored_find_phonemes(-2, phonemes, sentence)
# print(type(this_phone), this_phone[0])

class FP:
    '''returns a phoneme combination that user is seeking plus the prior 3 words. It is intended to be used to find rhyming couplets'''
    # def __init__(self, num_of_phonemes: int, ph_list: list[str], sentence: list[str]):
    def __init__(self, num_of_phonemes: int, ph_list: list, sentence: list, ngrm: int):
        self.num_of_phonemes = num_of_phonemes
        self.ph_list = ph_list
        self.sentence = sentence
        self.nrgram = ngrm

    def phonemeList(num_of_phonemes, ph_list, sentence) -> list:

        # def phoneme_list(self, num_of_phonemes, ph_list, sentence) ->list:
        '''return the a list of phonemes you are interested in'''
        output = []
        for i in sentence:
            sent = i.split()
            for j in range(len(sent)):
                word = re.sub(r'[^\w\s]', '', sent[j].lower())
                if word in prondict:
                    syl = prondict[word]
                    pho = syl[-1][num_of_phonemes:]
                    location = j
                    phrase = sent[location - 3:location + 1]
                    # if pho == ph_list then it's definitely longer than 1, so we don't need to check that
                    if pho == ph_list and len(word) > 3 and len(phrase) > 0:
                        # print('pho: ', pho)
                        # print('phrase: ', phrase)
                        output.append(phrase)
        return output

    def phonemeList_ngram(num_of_phonemes, ph_list, sentence, ngrm) -> list:

        # def phoneme_list(self, num_of_phonemes, ph_list, sentence) ->list:
        '''return the a list of phonemes you are interested in'''
        output = []
        for i in sentence:
            sent = i.split()
            for j in range(len(sent)):
                word = re.sub(r'[^\w\s]', '', sent[j].lower())
                if word in prondict:
                    syl = prondict[word]
                    pho = syl[-1][num_of_phonemes:]
                    location = j
                    phrase = sent[location - ngrm:location + 1]
                    # if pho == ph_list then it's definitely longer than 1, so we don't need to check that
                    if pho == ph_list and len(word) > 3 and len(phrase) > 0:
                        # print('pho: ', pho)
                        # print('phrase: ', phrase)
                        output.append(phrase)
        return output


def find_phonemes_ngram(num, ph_list, sentences,ngrm):
    output = []
    for i in sentences:
        sent = i.split()
        for j in range(len(sent)):
            word = re.sub(r'[^\w\s]', '', sent[j].lower())
            if word in prondict:
                syl = prondict[word]
                pho = syl[-1][num:]
                location = j
                phrase = sent[location-ngrm:location+1]
                # if pho == ph_list then it's definitely longer than 1, so we don't need to check that
                if pho == ph_list and len(word)>3 and len(phrase)>0:
                    # print('pho: ', pho)
                    # print('phrase: ', phrase)
                    output.append(phrase)
    return output


# print(type(Find_Phoneme))
# g = FP.phonemeList(-2, ['AH0', 'N'], sentence)
z = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, 5)
ph = FP.phonemeList_ngram(-2, ['AH0', 'N'], sentence, 3)

# print(ph[20])
# print(z[1], '\n')

# for i in range(5):
#     print(find_phonemes_ngram(-2, ['AH0', 'N'], sentence, i))
