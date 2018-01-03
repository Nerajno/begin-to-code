def calculate_score(word):
    vowel_count = 0
    consonant_count = 0
    for letter in word:
        letter = letter.lower()
        if letter in "aeiou":
            vowel_count += 1
        elif letter in "abcdefghijklmnopqrstuvwxyz":
            consonant_count += 1
    score = vowel_count - consonant_count
    return score

def get_color_code(word):
    score = calculate_score(word)
    if score >= 2:
        return 35
    elif score >= 1:
        return 34
    elif score >= 0:
        return 36
    elif score >= -1:
        return 32
    elif score >= -2:
        return 33
    else:
        return 31

def colorize_sentence(sentence):
    words = sentence.split(" ")
    result_words = []
    for word in words:
        color_code = get_color_code(word)
        result_words.append("\033[%dm%s\033[0m" % (color_code, word))
    result = " ".join(result_words)
    return result

if __name__ == '__main__':
    sentence = input("Enter a sentence: ")
    print(colorize_sentence(sentence))
