def find_substrings(s: str, words: list[str]) -> list[int]:
    if not words or not s:
        return []

    word_length = len(words[0])
    total_length = word_length * len(words)
    word_count = {}

    # Create a frequency map for words
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    result = []

    # Check each possible window in the string
    for i in range(word_length):
        left = i
        count = 0
        temp_word_count = {}

        for j in range(i, len(s) - word_length + 1, word_length):
            word = s[j:j + word_length]
            if word in word_count:
                temp_word_count[word] = temp_word_count.get(word, 0) + 1
                count += 1

                while temp_word_count[word] > word_count[word]:
                    left_word = s[left:left + word_length]
                    temp_word_count[left_word] -= 1
                    left += word_length
                    count -= 1

                if count == len(words):
                    result.append(left)
            else:
                temp_word_count.clear()
                count = 0
                left = j + word_length

    return result

print(find_substrings("barfoothefoobarman", ["bar","foo"]))
print(find_substrings("wordgoodgoodgoodbestword", ["word","good","best","word"]))
print(find_substrings("barfoofoobarthefoobarman", ["bar","foo","the"]))
print(find_substrings("ababababab", ["ababa", "babab"]))
print(find_substrings("ababaab", ["ab", "ba", "ba"]))
print(find_substrings("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a", "a", "a", "a", "a"]))