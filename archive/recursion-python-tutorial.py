#https://realpython.com/python-thinking-recursively/

#Example #1 from Tutorial
def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        print('base condition met')
        # print("1")
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        print(n)
        z = n * factorial_recursive(n-1)
        print('z is ', z)
        # return n * factorial_recursive(n-1)
        return z
    #I added the z and prints to see more clearly what was going on in the funciton


print('this is what is returned: ', factorial_recursive(5))
print('\n')

#maintaining state by threading it through the recursive call
def sum_recursive(current_number, accumulated_sum):
    # Base case
    # Return the final state
    if current_number == 11:
        return accumulated_sum

    # Recursive case
    # Thread the state through the recursive call
    else:
        print(current_number + 1, accumulated_sum, current_number)
        return sum_recursive(current_number + 1, accumulated_sum + current_number)

print('the final return is ', sum_recursive(1, 0))
print('\n')

#maintain state with global scope

# Global mutable state
current_number = 1
accumulated_sum = 0


def sum_recursive():
    global current_number
    global accumulated_sum
    # Base case
    if current_number == 11:
        return accumulated_sum
    # Recursive case
    else:
        print(current_number)
        accumulated_sum = accumulated_sum + current_number
        current_number = current_number + 1
        print(accumulated_sum, current_number)
        return sum_recursive()

print('the final return is ', sum_recursive())

print('\n')
#function that calculates the sum of all of the elements in a list
def list_sum_recursive(input_list):
    # Base case
    if input_list == []:
        return 0

    # Recursive case
    # Decompose the original problem into simpler instances of the same problem
    # by making use of the fact that the input is a recursive data structure
    # and can be deﬁned in terms of a smaller version of itself
    else:
        print('the input list is ', input_list)
        head = input_list[0]
        print('the head is ', head)
        smaller_list = input_list[1:]
        print('the smaller list is ', smaller_list)
        print('else function print ', head + list_sum_recursive(smaller_list))
        return head + list_sum_recursive(smaller_list)

print(list_sum_recursive([1, 2, 3]))
#Brent question, where does the addition happen in the sum of all the elemnents in a list funciton

# print(list_sum_recursive(['tirade', 'tired', 'tiered']))