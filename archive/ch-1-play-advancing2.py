nums = [0, 1, 2, 3, 4]
m = 4.35789/2.354
print('m is ', m)
# words = ["this", "that", "one", "and"]
words = ["butter", "chocolate", "smoke", "fire"]
def combine(iterations, nums):
    final = [] # create a list to hold all our lists
    if iterations > 0 and len(nums) >= iterations:
        if iterations == 1:
            final = final +[[nums[0]]]
        else:
            # print('altered array: ', nums[1:])
            final = final + [[nums[0]] + c for c in combine(iterations - 1, nums[1:])]
            # print('final after recursion: ', final)

            # add first [num] to "final array"
            # add rest of array recursively
        final = final + combine(iterations, nums[1:])
    return final

two_word_combos = []
three_word_combos = []

#can you go over how/why the i+1 is necessary in the combine?
for i in range(len(words)):
    print(i, ' combine: ', combine(i +1, words))
    if i == 1:
        twos = combine(i+1, words)
        two_word_combos.append(twos)
    if i == 2:
        threes = combine(i+1, words)
        three_word_combos.append(threes)
print(two_word_combos)
# print(three_word_combos)
# print('\n')

#the function above takes the words out of the list form and puts them into a more usable form
for w in range(len(two_word_combos)):
    for e in two_word_combos[w]:
        print(' '.join(e))
#A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.
#list comprehension example
squares = [x**2 for x in range(10)]
print(squares)

joined_words = [' '.join(e) for e in two_word_combos[w] for w in range(len(two_word_combos))]
print('the list comprehension version of joined_words ', joined_words)

s1 = 'abc'
s2 = 'def'
new_strings = [j + k for j in s1 for k in s2]
print(new_strings)
print('\n')
z = ' '
combo = ' '
#I'm combining the lists into a simple sentence here.
for w in range(len(two_word_combos)):
    for element in two_word_combos[w]:
        # print(' '.join(element))
        combo = combo + ' '.join(element) + ', '
        # print('the combo is: ', combo)
# print('the combo is: ', combo)
combi = ' '
combi = [combi + ' '.join(element) + ', ' for element in two_word_combos[w] for w in range(len(two_word_combos))]
print(combi)

for w in range(len(three_word_combos)):
    for e in three_word_combos[w]:
        # print(' '.join(e))
        z = z + ' '.join(e) + ', ' #join all of the elements in a list
tres_word_combi = ' '
tres_word_combi = [tres_word_combi + ' '.join(e) for e in three_word_combos[w] for w in range(len(three_word_combos))]
print(tres_word_combi)

print('the three word combo is: ', z)
sent_2_word = ('I am interested in ' + combo[1:-2] + ' and other toxic remedies.')
sent = ('I am interested in ' + z[1:-2]+ ' and the worlds biggest necklace.')
print(sent_2_word)
print(sent)
