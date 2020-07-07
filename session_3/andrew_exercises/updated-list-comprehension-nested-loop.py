import itertools
import random

#A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.
#list comprehension example
squares = [x**2 for x in range(10)]
print(squares)

# joined_words = [' '.join(e) for w in range(len(two_word_combos) )]

s1 = 'abc'
s2 = 'def'

for j in s1:
    for k in s2:
        print(j, k)

new_strings = [j + k for j in s1 for k in s2]
print(new_strings)

l1 = ["zero","one","two","three"]
l2 = ["four", "five","six", "seven"]

voices = ['sang', 'cried', 'stated', 'murmured', 'babbled', 'chattered',
          'ranted', 'whispered']
jj_nn = ['social engagement', 'institutional critique', 'activist art', 'urban life', 'everyday life', 'rigorous absurdity', 'traditional design', 'public space', 'artificial intelligence', 'biometric sensing', 'personal narrative',\
         'radical personhood', 'digital technology', 'digital art', 'systematic violence', 'feminist discourse', 'prosumer technology', 'contemporary life', 'further dialog', 'sublte manipulation', 'theoretical research', 'whole imagery', \
         'multi-channel video', 'multi-channel audio', 'hand-drawn rotoscoping', 'sound installation', 'cultural hybridity', 'popular culture', 'lush visuality', 'visual music', 'emotional expression', 'archival material', 'capitalist production','non-repesentational drawing', 'feminist art']



for i in range(len(l1)):
    for j in range(len(l2)):
        print(l1[i] + ' '+l2[j])
print('\n')

for i in range(len(l1)):
    for j in range (len(l1)):
        if l1[i] is not l1[j]:
            print(l1[i] +" "+l1[j])

#a version that would remove any combo that included the same items in a different order

#this will create a list with no duplicates/inverse duplicates
new_combos = []
conjunctions = ['and this artists work focuses on', 'and of course their famous work in', 'an interdisciplinary practice grounded in']
for i in range(len(jj_nn)):
    for j in jj_nn[i:]:
        if jj_nn[i] != j:
            new_combos.append(jj_nn[i].split(' ')[random.randint(0,1)]+" "+ j.split(' ')[random.randint(0,1)])

def combine(i, word_list):
    output = ''
    if (i <= 2):
        output = 'Our gallery has artwork with: ' + output
    output += word_list[i].split(' ')[random.randint(0,1)]+" "+ word_list[i].split(' ')[random.randint(0,1)] + combine(i-1, word_list[1:])
    print('output' + output)
    return output

print(combine(5, jj_nn))



#tried to get the removal of inverse duplicates, but couldn't figure it out
print('new combos is: ', new_combos)
new = []
for i in range(len(new_combos)):
    new = new_combos[i].split()
    for l in new_combos[i:]:
        m = l.split()
        # this will detect inverse duplicates in an existing list
        #if new[0] == m[1] and m[0] == new[1]:
                ## this is redundant -what's going on here?
#        if new[1] ==new[0] and new[0]==new[1]:
#            print('new 0:', new[0])
#            #print('new 1:', new[1])
#            print('match')
#            # print(new[1])
        # print(new[0] +" "+ new[1])

            # new.remove(new[1][0])

# print(new)






#
#
# def combine(num, words):
#     final = [] #a list called final is created within the function, this variable is returned when the funciton is completed
#     if num > 0 and len(words) >= num:
#         print ('num: ', num)
#         if num == 1:
#             final = final + [[words[0]]]
#             print ('final in if statement', final)
#         else:
#             final = final + [[words[0]] +
#                     c for c in combine(num - 1, words[1:])]
#             print('final in else statement', final)
#         final = final + combine(num, words[1:])
#     return final
#

#
# print('\n', 'the recursive one starts here')
# s=' '
#
# def combinations(s, l):
#     if l == 0:
#         print(s)
#     else:
#         combinations(s+s1[len(s1)-l], l-1)
#         combinations(s+s2[len(s2)-l], l-1)
#
# combinations(s, len(s1))
