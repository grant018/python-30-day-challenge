def is_anagram(word_one, word_two):
    w_one = {}
    w_two = {}
    for letter in word_one:
        w_one[letter] = w_one.get(letter, 0) + 1
    for letter in word_two:
        w_two[letter] = w_two.get(letter, 0) + 1
    return w_one == w_two

print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))   # False
print(is_anagram("rail safety", "fairy tales"))  # True

