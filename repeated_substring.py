# easy level

# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

# the fastest version:
# def rep_substring_pat(s: str) -> bool:
#   return s in (s+s)[1:-1]

def subdivise_string(s: str) -> tuple:
    a = s[:len(s)//2]
    b = s[len(s)//2:]
    return (a, b)

def search_repeated_substring(s: str) -> bool:
    if not check_string(s):
        return False

    # better version:
    # for i in range(1, len(s)):
    #   if s[:i] * int(len(s)/i) ==s:
    #       return True

    if len(s) % 2 == 0:
        a, b = subdivise_string(s)
        if a == b:
            return True

    substring = ""
    for letter in s:
        substring += letter
        number_sub = s.count(substring)
        if (number_sub * len(substring)) == len(s) and substring != s:
            return True
    return False

def check_string(s: str) -> bool:
    if len(s) < 1 or len(s) > 10**4:
        return False
    return True

s1 = "abcabc"
s2 = "ababab"
s3 = "abcabcabcabc"
s4 = "abcabcabc"

print(search_repeated_substring(s1))
print(search_repeated_substring(s2))
print(search_repeated_substring(s3))
print(search_repeated_substring(s4))