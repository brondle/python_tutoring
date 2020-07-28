
__author__ = 'Nick Montfort'
__license__ = 'ISC'
__version__ = '1.0'


#### GENERAL
# he is importing textblob's Word module
from textblob import Word
#this section is setting up the chapter titles in the whole book
def next_section(num):
    text.append('\n\\newpage')
    text.append('\n# ' + num + '\n\n')

text = []
#this is a dictionary with key/value pairs that he is using to make a word that referes to a number
spelled_out = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty'
}


#### THE VOICES
#there is an empty list called text that is being added to with the chapter name and then the chapter text with line breaks
text.append('\n# I\n\n')
#this is the main function that is doing most of the heavy lifting in the program
#in this function we are passing in two variables to be processed
def combine(num, words):
    final = [] #a list called final is created within the function, this variable is returned when the funciton is completed
    if num > 0 and len(words) >= num:
        print ('num: ', num)
        if num == 1:
            final = final + [[words[0]]]
            print ('final in if statement', final)
        else:
            final = final + [[words[0]] +
                    c for c in combine(num - 1, words[1:])]
            print('final in else statement', final)
            # for c in combine(num - 1, words[1:]):
            #     print('c: ')
        final = final + combine(num, words[1:])
    return final

## In Watt the voices = ['sang', 'cried', 'stated', 'murmured']
## And Watt understood = ['all', 'much', 'little', 'nothing']
## Here the voices did eight things and there are eight levels:
voices = ['sang', 'cried', 'stated', 'murmured', 'babbled', 'chattered',
          'ranted', 'whispered']
understood = ['all', 'most', 'much', 'half', 'little', 'less', 'bits',
              'nothing']
para = ''
preface = ', and sometimes they '
#I understand what is mostly happening in this funciton, but I don't get how on the first pass through the first 'sometimes' doesn't ahve an 'and' in front
for num in range(len(voices)): #num is an iterating variable that counts through the number of items (a list of strings) in voices, it is currently 8
   for word_list in combine(num + 1, voices):#this line calls the function above, with the index number and the word from the list
       #for each index item in the voices list, send them into the combine function and add them to the varaible called para.
       para = para + preface + ' and '.join(word_list) #the ' and '.join(word_list) takes the words out of a list form and puts them into a string, with ' and ' in between each item
       print('word list: ', combine(num + 1, voices))
       if len(word_list) == 1: #this is a conditional that says, if the word list is down to 1, the paragraph will be different from the prior versions
           para = para + ' only'
##the [5:] is saying start the paragraph after the 5th item counting from 0.
#para = ('Watt heard voices. Now these voices,' + para[5:] +
#    ', all together, at the same time, as now, to mention ' +
#    'only these ' + spelled_out[len(voices)] + ' kinds of voices, for ' +
#    'there were others. And sometimes Watt understood ' +
#    ', and sometimes he understood '.join(understood) + ', as now.') #the majority of the text we are adding happens at para[5:]
#text.append(para)
#I added a print funciton into chapter one, so we didn't have to print out the book in order to run the program
print(text)
