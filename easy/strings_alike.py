# easy level

# determine if string halves are alike
# You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.
# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.
# Return true if a and b are alike. Otherwise, return false.

def check_and_compare(s : str):
    if not check_string(s):
        print("String incorrect.")
        return None
    if compare_halves(s):
        print(f"The string halves of {s} are alike.")
        return True
    else:
        print(f"The string halves of {s} are not alike.")
        return False

def compare_halves(s: str) -> bool:
    s = s.lower()
    a = s[:(len(s)//2)]
    b = s[(len(s)//2):]
    vowels_a = vowels_count(a)
    vowels_b = vowels_count(b)
    if vowels_a == vowels_b:
        return True
    else:
        return False

def vowels_count(s: str) -> int:
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for letter in s:
        if letter in vowels:
            count += 1
    return count


def check_string(s: str) -> bool:
    if len(s) < 2 or len(s) > 1000:
        return False
    if len(s) % 2 == 1:
        return False
    return True

s1 = "book"
s2 = "textbook"

check_and_compare(s1)
check_and_compare(s2)