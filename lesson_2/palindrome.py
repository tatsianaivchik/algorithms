#reverse of the string is the same as string

def is_palindrome(s):
    return s == s[::-1]

s1 = "radar"
s2 = "radax"
result = is_palindrome(s2)
print(result)
