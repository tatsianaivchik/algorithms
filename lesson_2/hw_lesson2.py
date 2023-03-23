# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

def split_into_two(s):
    if len(s) % 2 == 0:
        return s[len(s)//2:] + s[:len(s)//2]
    else:
        return s[len(s)//2+1:] + s[:len(s)//2+1]

string1 = 'bbbbbcaaaaa'
string2 = 'bbbbbcaaaa'
# print(split_into_two(string1))
# print(split_into_two(string2))



# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.

def verify_all_chars_unique(s):
    new_str = ""
    for char in s:
        if char not in new_str:
            new_str += char
        else:
            return False
    return True

    # return len(set(s)) == len(s) <- 

s1 = 'abcde'
s2 = 'aabcde'
print(verify_all_chars_unique(s2))
print(verify_all_chars_unique(s1))

