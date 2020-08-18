import re
# is this being used?
# from helper import *
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

