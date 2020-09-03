import random

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
            output = output + [[word_list[random.randint(0,i)].split(' ')[random.randint(0, 1)]]]


        else:
            output += [word_list[i].split(' ')[random.randint(0,1)]]+" "+ [word_list[i].split(' ')[random.randint(0,1)] + combine(i-1, word_list[1:])]
            print('output: ', output)
            # output = output + [[word_list[random.randint(0,i)].split(' ')[random.randint(0, 1)]] + c for c in combine(random.randint(1,i), word_list[random.randint(0, 1):])]

    # output = output + [[word_list[i].split(' ')[random.randint(0, 1)]] +  c for c in combine(i - 1, word_list[i:])]
    return output


print(combine(5, i_verb))
#how can we alter just the numbers (how we are playing with i) how many elements of
#what if you divide the i, multiply, what about a fibonacci sequence. just as much as the output is a work of art


def combine(num, words):
    final = []
    if num > 0 and len(words) >= num:
        print ('num: ', num)
        if num == 1:
            final = final + [[words[0]]]
            print ('final in if statement', final)
        else:#the double array/list places in a subarray, it concatenates it to a list
            final = final + [[words[0]] +
                    c for c in combine(num - 1, words[1:])]
            # for c in combine(num - 1, words[1:]):  
            #     print(‘c: ‘, c) 

            print('final in else statement', final) #the line above builds a single array each time it is run,
            # in other other words the internal array builds one and the one below builds the whole.
        final = final + combine(num, words[1:])#this one builds the array of arrays. in the program flow,
    return final
