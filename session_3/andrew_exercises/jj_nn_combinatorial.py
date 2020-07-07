from random import choice

jj_nn = ['social engagement', 'institutional critique', 'activist art', 'urban life', 'everyday life', 'rigorous absurdity', 'traditional design', 'public space', 'artificial intelligence', 'biometric sensing', 'personal narrative',\
         'radical personhood', 'digital technology', 'digital art', 'systematic violence', 'feminist discourse', 'prosumer technology', 'contemporary life', 'further dialog', 'sublte manipulation', 'theoretical research', 'whole imagery', \
         'multi-channel video', 'multi-channel audio', 'hand-drawn rotoscoping', 'sound installation', 'cultural hybridity', 'popular culture', 'lush visuality', 'visual music', 'emotional expression', 'archival material', 'capitalist production','non-repesentational drawing', 'feminist art']
type_of_work = ["painting", "drawing", "video", "sound", "multi-media", "poetry"]
type_of_installation = ['interactive', 'sculptural', 'immersive', 'hybrid', 'holistic', 'multidisciplinary', 'conceptual', 'critical', 'virtual', 'physical', 'temporary', 'public', 'subversive']
type_of_practice = ['intersectional', 'interdisciplinary', 'hybrid', 'holistic', 'spiritual', ]
jj = []
nn = []
split_jj_nn = []
for i in range(len(jj_nn)):
    sep = jj_nn[i].split()
    jj.append(sep[0])
    nn.append(sep[1])
    split_jj_nn.append(sep[0]+ " "+ sep[1])
# print(jj)
# print(nn)

def jj_nn_combine():
    adj = choice(jj)
    noun = choice(nn)
    return adj + " " + noun
def art_type():
    at = choice(type_of_work)
    return at
def installation_type():
    it = choice(type_of_installation)
    return it

art_jibberish = ("I create " + art_type() + " and " + installation_type() +  " installations that combine " + jj_nn_combine() + ", " + jj_nn_combine() \
                 + ", " + jj_nn_combine() + ", " + jj_nn_combine() + " and "+  jj_nn_combine() + " together in an interdisciplinary practice." )
print(art_jibberish)

# for i in range(len(jj_nn[:6])):
#     for j in range(len(jj_nn[:6])):

# possible_combos = []
# print(split_jj_nn)
# for i in range(len(split_jj_nn)):
#     for j in range(len(split_jj_nn)):
#         if(split_jj_nn[i] is not split_jj_nn[j]):
            # possible_combos.append((split_jj_nn[i] +" "+split_jj_nn[j]))
# print(possible_combos)



