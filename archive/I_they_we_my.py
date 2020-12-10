import itertools
import random
import repeating

jj_nn = ['social engagement', 'institutional critique', 'activist art', 'urban life', 'everyday life', 'rigorous absurdity', 'traditional design', 'public space', 'artificial intelligence', 'biometric sensing', 'personal narrative',\
         'radical personhood', 'digital technology', 'digital art', 'systematic violence', 'feminist discourse', 'prosumer technology', 'contemporary life', 'further dialog', 'sublte manipulation', 'theoretical research', 'whole imagery', \
         'multi-channel video', 'multi-channel audio', 'hand-drawn rotoscoping', 'sound installation', 'cultural hybridity', 'popular culture', 'lush visuality', 'visual music', 'emotional expression', 'archival material', 'capitalist production','non-repesentational drawing', 'feminist art']

conjunctions = ['and this artists work focuses on', 'and of course their famous work in', 'an interdisciplinary practice grounded in']

they_verb =[('they', 'strive'), ('they', 'conjure'), ('they', 'choose'), ('they', 'arise'), ('they', 'occupy'), ('they', 'reside'), ('they', 'speak'), ('they', 'start'), ('they', 'work'), ('they', 'produce'), ('they', 'bridge'), ('they', 'are'), ('they', 'have'), ('they', 'morph'), ('they', 'perceive')]
i_verb = ['I create', 'I imagine', 'I build', 'I ask', 'I hope', 'I explore', 'I employ', 'I construct', 'I animate', 'I leverage', 'I excavate', 'I immerse', 'I seek', 'I collaborate', 'I write', 'I integrate', 'I manipulate', 'I foreground', 'I choose', 'I examine', 'I aim', 'I present', 'I utilize', 'I re-articulate', 'I layer', 'I address', 'I question', 'I combine', 'I work', 'I attempt', 'I like', 'I collect', 'I bundle', 'I mimic', 'I prioritize', 'I reflect', 'I borrow', 'I interrogate', 'I refuse', 'I consider', 'I draw', 'I intend', 'I look', 'I document', 'I investigate', 'I strive', 'I search', 'I alter', 'I author', 'I incorporate', 'I photograph', 'I remain', 'I treat', 'I populate', 'I accomplish']
my_phrase = ['my practice', 'my artwork', 'my work—behavior', 'my work', 'my voice', 'my portfolio', 'my exhibition', 'my project', 'my research', 'my background', 'my interest', 'my art', 'my way', 'my father', 'my exploration', 'my body', 'my audience', 'my perfectionist', 'my identity', 'my mother', 'my sculpture', 'my job', 'my journey', 'my time', 'my alter', 'my imagery', 'my theatre', 'my career', 'my purpose', 'my method', 'my aim', 'my site', 'my process', 'my desire', 'my past']
tv_length = len(they_verb)
they_string = ''
i_string = ''
seperator = ''

def converttostr(input_seq, seperator):
   # Join all the strings in list
   final_str = seperator.join(input_seq)
   return final_str

def they():
    rc = int(random.random()*tv_length)
    they_string = (they_verb[rc][0] + " "+ they_verb[rc][1])
    return they_string
def i_combo():
    rc = int(random.random()*len(i_verb))
    i_string = i_verb[rc]
    return i_string
def my_phrase_combo():
    rc = int(random.random()*len(my_phrase))
    my_string = my_phrase[rc]
    return my_string
co = 0
reapeat_num = 4

def print_seq():
    global co
    print(they()+'.')
    print(i_combo()+'.')
    print("I am ", my_phrase_combo()+'.')
    print('\n')
    co = co + 1
    if co > reapeat_num:
        r.stop()
    return co

# this is calling upon the Repeat class that I made in the 'repeating' module.
# it takes two arguments, the duration to wait and the name of the function you'd like to repeat
# r = repeating.Repeat(1, repeatRandomWords)
# put r.stop in the repeating function to stop when a certain count is hit
r = repeating.Repeat(2, print_seq)
r.start()