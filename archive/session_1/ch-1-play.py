nums = [0, 1, 2, 3, 4]


def combine(iterations, nums):
    print('internal combine: ')
    print('iterations: ', iterations)
    final = [] # create a list to hold all our lists
    if iterations > 0 and len(nums) >= iterations:
        print('[[nums[0]]:', [[nums[0]]])
        if iterations == 1:
            final = final +[[nums[0]]]
            print('bottom-level final: ', final)
        else:
            print('altered array: ', nums[1:])
            final = final + [[nums[0]] + c for c in combine(iterations - 1, nums[1:])]
            print('final after recursion: ', final)
            # add first [num] to "final array"
            # add rest of array recursively
        final = final + combine_external(iterations, nums[1:])
    return final

def combine_external(iterations, nums):
    print('external combine: ')
    print('iterations: ', iterations)
    final = [] # create a list to hold all our lists
    if iterations > 0 and len(nums) >= iterations:
        print('[[nums[0]]:', [[nums[0]]])
        if iterations == 1:
            final = final +[[nums[0]]]
            print('bottom-level final: ', final)
        else:

            print('altered array: ', nums[1:])
            final = final + [[nums[0]] + c for c in combine(iterations - 1, nums[1:])]
            print('final after recursion: ', final)
            # add first [num] to "final array"
            # add rest of array recursively
        final = final + combine_external(iterations, nums[1:])
    return final


for i in range(len(nums)):
    print('combine: ', combine(i + 1, nums))

