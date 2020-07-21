import nltk.corpus
from nltk.text import Text
from nltk.corpus import PlaintextCorpusReader
# corpus_root = '/Users/ademirji/PycharmProjects/NaturalLangage/Tuesdays/python_tutoring/session_4/'



corpus_root = '/Users/ademirji/PycharmProjects/NaturalLangage/texts'


#to be able to apply NLTK concordance features to a text file of your own do this:
# point the corpus reader to your folder
wordlists = PlaintextCorpusReader(corpus_root, '.*')
my_text = wordlists.words(fileids=["artistStatements.txt"])
textList = Text(my_text)
textList.concordance('explore')
textList.similar('explore')
textList.common_contexts(['explore', 'navigate'])
textList.dispersion_plot(['community', 'soul', 'AI', 'reveal'])

# print(wordlists.fileids())
# print(wordlists.words(fileids=["artistStatements.txt"])[:50])
# my_joined_text = ' '.join(my_text)
# print(' '.join(my_text))

#this was an online example
# textListNLTK = Text(textList)
# textListNLTK.concordance('CNA')
# moby = Text(nltk.corpus.gutenberg.words('melville-moby_dick.txt'))
# textList = Text(nltk.corpus.gutenberg.words('YOUR FILE NAME HERE.txt'))
# textList.concordance('CNA')

# text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "liberty"])

