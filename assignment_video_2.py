# Get element from second position to fifth position from list - [1, 2, 3, 4, 5, 6]

a = [1, 2, 3, 4, 5, 6]
print(a[slice(1, 5)])


# Check if string palindrome or not “ab”, “abc”, “aba”

def reverse(s):
    return s[::-1] == s


listString = ["ab", "abc", "aba"]
isPalindrome = [reverse(i) for i in listString]
print(isPalindrome)
