def reverse_word(word):
    result = ""
    for letter in word:
        result = letter + result
    return result

def reverse_all_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        result_word = reverse_word(word)
        result_words.append(result_word)
    result_phrase = " ".join(result_words)
    return result_phrase

# print(reverse_word("basketball"))
# print(reverse_word("bananas"))

print(reverse_all_words("pass the banana"))
print(reverse_all_words("throw the frisbee"))
