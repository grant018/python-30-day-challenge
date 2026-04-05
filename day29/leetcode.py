def is_palindrome(word: str):
    cleaned = "".join(letter for letter in word.lower() if letter != " ")
    return cleaned == cleaned[::-1]

def flatten(nested: list[list]):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(is_palindrome("racecar"))         # True
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("hello"))         # False
print(flatten([1, [2, 3], [4, [5, 6]]]))    # [1, 2, 3, 4, 5, 6]


