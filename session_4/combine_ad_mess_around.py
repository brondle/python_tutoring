import random
mywords = ['trounced', 'bounced', 'pounced', 'throbbed', 'sobbed', 'minced',
          'winced', 'whistled']
sounds = ['groaned', 'whistled', 'waivered', 'fluttered', 'coughed', 'stuttered',
          'muttered', 'choked']
voices = ['sang', 'cried', 'stated', 'murmured', 'babbled', 'chattered',
          'ranted', 'whispered']
jj_nn = ['social engagement', 'institutional critique', 'activist art', 'urban life', 'everyday life', 'rigorous absurdity', 'traditional design', 'public space', 'artificial intelligence', 'biometric sensing', 'personal narrative',\
         'radical personhood', 'digital technology', 'digital art', 'systematic violence', 'feminist discourse', 'prosumer technology', 'contemporary life', 'further dialog', 'sublte manipulation', 'theoretical research', 'whole imagery', \
         'multi-channel video', 'multi-channel audio', 'hand-drawn rotoscoping', 'sound installation', 'cultural hybridity', 'popular culture', 'lush visuality', 'visual music', 'emotional expression', 'archival material', 'capitalist production','non-repesentational drawing', 'feminist art']

they_verb =[('they', 'strive'), ('they', 'conjure'), ('they', 'choose'), ('they', 'arise'), ('they', 'occupy'), ('they', 'reside'), ('they', 'speak'), ('they', 'start'), ('they', 'work'), ('they', 'produce'), ('they', 'bridge'), ('they', 'are'), ('they', 'have'), ('they', 'morph'), ('they', 'perceive')]
i_verb = ['I create', 'I imagine', 'I build', 'I ask', 'I hope', 'I explore', 'I employ', 'I construct', 'I animate', 'I leverage', 'I excavate', 'I immerse', 'I seek', 'I collaborate', 'I write', 'I integrate', 'I manipulate', 'I foreground', 'I choose', 'I examine', 'I aim', 'I present', 'I utilize', 'I re-articulate', 'I layer', 'I address', 'I question', 'I combine', 'I work', 'I attempt', 'I like', 'I collect', 'I bundle', 'I mimic', 'I prioritize', 'I reflect', 'I borrow', 'I interrogate', 'I refuse', 'I consider', 'I draw', 'I intend', 'I look', 'I document', 'I investigate', 'I strive', 'I search', 'I alter', 'I author', 'I incorporate', 'I photograph', 'I remain', 'I treat', 'I populate', 'I accomplish']
my_phrase = ['my practice', 'my artwork', 'my work—behavior', 'my work', 'my voice', 'my portfolio', 'my exhibition', 'my project', 'my research', 'my background', 'my interest', 'my art', 'my way', 'my father', 'my exploration', 'my body', 'my audience', 'my perfectionist', 'my identity', 'my mother', 'my sculpture', 'my job', 'my journey', 'my time', 'my alter', 'my imagery', 'my theatre', 'my career', 'my purpose', 'my method', 'my aim', 'my site', 'my process', 'my desire', 'my past']

def combine(i, word_list):
    output = []
    if i > 0 and len(word_list) >= i:
        if (i == 1):
            print('output2:', ' '.join(output))
            # output = output + [[word_list[i].split(' ')[random.randint(0, 1)]]]
            # output = output + [[word_list[random.randint(0,i)].split(' ')[random.randint(0, 1)]]]
            r_list_choice2 = int(len(word_list) * random.random())
            # output = output + [word_list[r_list_choice2].split(' ')]
            output = output + [word_list[i].split()]
        else:
            print('output: ', output)
            print("i is ", i)
            output = output + [[word_list[i]] + c for c in combine(i-1, word_list[1:])]
            #output = output + [[word_list[i].split(' ')[random.randint(0,1)]] + c for c in combine(i-1, word_list[1:])]
            #r_list_choice = int(len(word_list)*random.random())
            #output = output + [word_list[r_list_choice].split() + c for c in combine(i-1, word_list[1:])]

            # output = output + [word_list[i].split(' ')[random.randint(0,1)]] + " "+[word_list[i].split(' ')[random.randint(0,1)] + combine(i-1, word_list[1:])]
            # output += [word_list[i].split(' ')[random.randint(0,1)]]+" "+ [word_list[i].split(' ')[random.randint(0,1)] + combine(i-1, word_list[1:])]

            print('output: ', output)

    # output = output + [[word_list[i].split(' ')[random.randint(0, 1)]] +  c for c in combine(i - 1, word_list[i:])]
    return output


print(combine(6, jj_nn))

sentence = ' '
the_whole =[]
preface = ' and '
new_string = ' '

for i in range(1):
    for w_list in combine(6, jj_nn):
        print('w_list i is ', w_list[i])
        new_string = new_string+' '.join(w_list)
print('new string is ', new_string)

for i in range(1):
    for w_list in combine(6, jj_nn):
        sentence = sentence + preface + ' '.join(w_list)+','

print('\n')
#how can we alter just the numbers (how we are playing with i) how many elements of
#what if you divide the i, multiply, what about a fibonacci sequence.

the_combos = ' '
sentence = ('I am an artist who explores' + new_string + ' to create a transcendant experience in the viewer/listener.')
the_whole.append(sentence)
print(the_whole)
