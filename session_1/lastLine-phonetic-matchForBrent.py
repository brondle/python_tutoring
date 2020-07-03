import re
from helper import *
from nltk.corpus import PlaintextCorpusReader
import nltk

prondict = nltk.corpus.cmudict.dict()

#retrieve corpus
corpus_root = './'
corpus = PlaintextCorpusReader(corpus_root, '.*')
colorsText = corpus.raw('lastLines.txt')

cWord = colorsText.splitlines()
cWord2 = colorsText.splitlines()
prondict = nltk.corpus.cmudict.dict()


#vowels
thisSound = [['AA0'], ['AA1'], ['AA2'], ['AE0'], ['AE1'], ['AE2'], ['AH0'], ['AH1'], ['AH2'], ['AO0'], ['AO1'], ['AO2'],
             ['AW0'], ['AW1'], ['AW2'], ['AX0'], ['AX1'], ['AX2'], ['AXR'], ['AY0'], ['AY1'], ['AY2'], ['EH0'], ['EH1'],
             ['EH2'], ['ER0'], ['ER1'],['ER2'], ['EY0'], ['EY1'], ['EY2'], ['IH0'], ['IH1'], ['IH2'], ['IX0'], ['IX1'],
             ['IX2'], ['IY0'], ['IY1'], ['IY2'], ['OW0'], ['OW1'], ['OW2'], ['OY0'], ['OY1'], ['OY2'], ['UH0'], ['UH1'],
             ['UH2'], ['UW0'], ['UW1'], ['UW2'], ['UX0'], ['UX1'], ['UX2']]

thisSound2 = [['AA0'], ['AA1'], ['AA2'], ['AE0'], ['AE1'], ['AE2'], ['AH0'], ['AH1'], ['AH2'], ['AO0'], ['AO1'], ['AO2'],
             ['AW0'], ['AW1'], ['AW2'], ['AX0'], ['AX1'], ['AX2'], ['AXR'], ['AY0'], ['AY1'], ['AY2'], ['EH0'], ['EH1'],
             ['EH2'], ['ER0'], ['ER1'],['ER2'], ['EY0'], ['EY1'], ['EY2'], ['IH0'], ['IH1'], ['IH2'], ['IX0'], ['IX1'],
             ['IX2'], ['IY0'], ['IY1'], ['IY2'], ['OW0'], ['OW1'], ['OW2'], ['OY0'], ['OY1'], ['OY2'], ['UH0'], ['UH1'],
             ['UH2'], ['UW0'], ['UW1'], ['UW2'], ['UX0'], ['UX1'], ['UX2']]


#how many phones?
#if the syllables are at the end of the word you need a negative number
# phoneNum = 1
phoneNum = -1
#if syllables are at the beginning of the word, you need a positive number
# phoneNum = 2
phoneNum2 = -1 #refactor here (does this need to be here?)

#last word first phoneme
for s in range(0, len(thisSound)):
    print('this is the phoneme: ', thisSound[s])
    for line in cWord:
        lineList = line.split()
        # theWord = re.sub(r'[^\w\s]','',lineList[-1]).lower()
        theWord = re.sub(r'[^\w\s]','',lineList[0]).lower()


        if theWord in prondict and theWord.isalpha():
            syllable = prondict[theWord]
            phoneme = syllable[-1][phoneNum:]

            if thisSound[s] == phoneme:
                listByPh = line

                #first word, first phoneme
                for line2 in cWord2:
                    lineList2 = line2.split()
                    theWord2 = re.sub(r'[^\w\s]', '', lineList2[-1]).lower()

                    if theWord2 in prondict and theWord2.isalpha():
                        syllable2 = prondict[theWord2]
                        phoneme2 = syllable2[-1][phoneNum2:]
                        # if thisSound2[s2] == phoneme2:
                        if thisSound2[s] == phoneme2:
                            listByPh2 = line2
                            if theWord != theWord2 and theWord[:-1] != theWord2 and theWord2[:-1] != theWord:
                                #if word/phoneme search 1 does not equal word search phoneme 2 (or a plural of the word) then print
                                print(listByPh, listByPh2)
