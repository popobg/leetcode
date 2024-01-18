# You are given a string s and an array of strings words. All the strings of words are of the same length.
# A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.

# Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.
# s and each word of words are lowercase English letters.

import os, json, time
from pathlib import Path

def make_relative_path(relative_path):
    return os.path.join(Path(__file__).parent, relative_path)

def find_substrings(s: str, words: list[str]) -> list[int]:
    """search for the associations of words in the string s
    and return the starting indices of all concatenated substrings"""

    len_concat_substring = len(words) * len(words[0])

    if len(s) < len_concat_substring:
        return []

    # making a dictionnary with the list of words to find and their occurences in the list of words
    dict_words = {}
    minimal_index = len(s)

    for word in words:
        if word in dict_words:
            continue

        dict_words[word] = words.count(word)

        ind = s.find(word)
        if ind == -1:
            return []

        elif minimal_index == 0:
            pass

        elif ind < minimal_index:
            minimal_index = ind

    # a list of the words without duplicate
    unique_words = list(dict_words.keys())

    substrings_index = []

    while minimal_index != -1:
        substring = s[minimal_index:(minimal_index + len_concat_substring)]

        if all_substrings(substring, words, dict_words):
            substrings_index.append(minimal_index)

        minimal_index = determine_minimal_index(s, unique_words, (minimal_index + 1), (len(s) - (len_concat_substring - len(words[0]))))

    return substrings_index


def all_substrings(substr: str, words: list[int], dic: dict[str:int]) -> bool:
    """return True if all the words and only them are in the substring
    return False otherwise"""
    # the dict with the words of the substring and their occurences
    dic_substr = {}

    for i in range(0, len(substr), len(words[0])):
        word = substr[i:i + len(words[0])]

        dic_substr[word] = dic_substr.get(word, 0) + 1

    # are the dic with words and the dic of the substring the same?
    if dic == dic_substr:
        return True

    return False


def determine_minimal_index(s: str, words: list[int], start_index, end_index) -> int:
    """finding the next minimal index of a target word in the string"""
    minimal_index = len(s)

    for word in words:
        # function find() returns -1 if item not found
        # function index() raises an error
        ind = s.find(word, start_index, end_index)

        if ind != -1 and ind < minimal_index:
            minimal_index = ind

    if minimal_index == len(s):
        return -1

    return minimal_index


# MAIN

print(find_substrings("barfoothefoobarman", ["bar","foo"]))
print(find_substrings("wordgoodgoodgoodbestword", ["word","good","best","word"]))
print(find_substrings("barfoofoobarthefoobarman", ["bar","foo","the"]))
print(find_substrings("ababababab", ["ababa", "babab"]))
print(find_substrings("ababaab", ["ab", "ba", "ba"]))
print(find_substrings("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a", "a", "a", "a", "a"]))

with open(make_relative_path("string_concat.txt"), "r", encoding = "utf-8") as f:
    string_a = f.read()

with open(make_relative_path("words.json"), "r", encoding = "utf-8") as f:
    words_a = json.load(f)

st = time.time()
print(find_substrings(string_a, words_a))
et = time.time()

print("Overall time: ", et - st)