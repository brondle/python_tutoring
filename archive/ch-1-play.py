nums = [0, 1, 2, 3, 4]

m = 4.35789/2.354
print('m is ', m)

words = ["this", "that", "one", "and"]

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

# for i in range(len(nums)):
#     print('combine: ', combine(i + 1, nums))
for i in range(len(words)):
    print(i, ' combine: ', combine(i +1, words))


#figure out how to remove the list or to make a big list of combos then print them into a more readable form