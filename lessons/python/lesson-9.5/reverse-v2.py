def break_words(phrase):
    return phrase.split(" ")

def reverse_word(word):
    result = ""
    for letter in word:
        result = letter + result
    return result

def join_words(words):
    return " ".join(words)

def reverse_each_word(words):
    result_words = []
    for word in words:
        result_word = reverse_word(word)
        result_words.append(result_word)
    return result_words

def reverse_all_words(phrase):
    words = break_words(phrase)
    result_words = reverse_each_word(words)
    result_phrase = join_words(result_words)
    return result_phrase

# print(reverse_word("basketball"))
# print(reverse_word("bananas"))

reverse_all_words("pass the banana")
reverse_all_words("throw the frisbee")
