
def convert_words(phrase, fn):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        result_word = fn(word)
        result_words.append(result_word)
    result = " ".join(result_words)
    return result

def reverse_word(word):
    result = ""
    for letter in word:
        result = letter + result
    return result

def piglatin(word):
    vowels = "aeiou"
    if word[0] not in vowels:
        if word[1] not in vowels:
            return word[2:] + word[:2] + "ay"
        else:
            return word[1:] + word[:1] + "ay"
    else:
        return word + "way"

print(convert_words("what the heck dude", reverse_word))
print(convert_words("what the heck dude", piglatin))
