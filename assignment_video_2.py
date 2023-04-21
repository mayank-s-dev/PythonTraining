# Get element from second position to fifth position from list - [1, 2, 3, 4, 5, 6]
def slice_it(input):
    return input[slice(1, 5)]


a = [1, 2, 3, 4, 5, 6]
response = slice_it(a)
print(response)


# Check if string palindrome or not “ab”, “abc”, “aba”

def reverse(s):
    return s[::-1] == s


def check_palindrome(inputList):
    res = [reverse(i) for i in inputList]
    return res


response = check_palindrome(["nayan", "abc"])
print("Palindrome", response)


# Check if string contains repeated characters “aab”, “abc”, “def”

def is_repetition(input_str):
    test_dict = {}
    for i in input_str:
        if test_dict.get(i) is None:
            test_dict[i] = 1
        else:
            test_dict[i] = test_dict[i] + 1
            return True

    return False


def check_repetition(inputList):
    res = [is_repetition(i) for i in inputList]
    return res


response = check_repetition(["nayan", "abc"])
print("Repetition", response)
