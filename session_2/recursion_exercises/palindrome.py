test_palindrome="ttarataratt"

def is_palindrome(string):
    if len(string) == 0:
        return True
    else:
        if string[0] == string[len(string)-1]:
            return is_palindrome(string[1:-1])
        else:
            return False

print(is_palindrome(test_palindrome))

