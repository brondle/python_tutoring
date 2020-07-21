import random

voices = ['sang', 'cried', 'stated', 'murmured', 'babbled', 'chattered',
          'ranted', 'whispered']
jj_nn = ['social engagement', 'institutional critique', 'activist art', 'urban life', 'everyday life', 'rigorous absurdity', 'traditional design', 'public space', 'artificial intelligence', 'biometric sensing', 'personal narrative',\
         'radical personhood', 'digital technology', 'digital art', 'systematic violence', 'feminist discourse', 'prosumer technology', 'contemporary life', 'further dialog', 'sublte manipulation', 'theoretical research', 'whole imagery', \
         'multi-channel video', 'multi-channel audio', 'hand-drawn rotoscoping', 'sound installation', 'cultural hybridity', 'popular culture', 'lush visuality', 'visual music', 'emotional expression', 'archival material', 'capitalist production','non-repesentational drawing', 'feminist art']

def combine(i, word_list):
    output = []
    if i > 0 and len(word_list) >= i:
        if (i == 1):
            print('output2:', ' '.join(output))
            # output = output + [[word_list[i].split(' ')[random.randint(0, 1)]]]
            output = output + word_list[i].split(' ')

        else:
            output += word_list[i].split(' ')+" " + combine(i-1, word_list[1:])

           # output += word_list[i].split(' ')[random.randint(0,1)]+" "+ word_list[i].split(' ')[random.randint(0,1)] + combine(i-1, word_list[1:])
            print('output: ', output)
            # output = output + [[word_list[i].split(' ')[random.randint(0, 1)]] +  c for c in combine(i - 1, word_list[i:])]
    return output


print(combine(5, jj_nn))