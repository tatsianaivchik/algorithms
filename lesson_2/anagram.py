# is another string contains same char but in diff order?

def is_anagram(s1, s2):
    # if len(s1) != len(s2):
    #     return False
    if sorted(s1) == sorted(s2):
        return True
    return False

test_st1 = "abcde"
test_st2 = "abced"
result = is_anagram(test_st2, test_st1)
print(result)