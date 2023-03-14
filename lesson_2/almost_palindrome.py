# given a str, you might delete at most one char. Ckeck if you can make a palindrome

def is_almost_palindrome(s):
    for i in range(len(s)):
        temp_s = s[0:i] + s[(i+1):]
        if temp_s == temp_s[::-1]:
            return True
    return False

s1 = "radkar"
s2 = "radario"

result = is_almost_palindrome(s2)
print(result)
