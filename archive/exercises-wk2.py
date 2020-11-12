
this_list = ['this', 'that', 'one']

def my_first_recursion(my_list):
    if len(my_list) == 1:
        print(my_list[0])
        return 'finished'

    else:
        head = my_list[0]
        print(head)
        tail = my_list[1:]
        print(tail)
        my_first_recursion(tail)


print('the function is returning', my_first_recursion(this_list))

