sentence = input("Enter a sentence: ")
words = sentence.split(" ")
result_words = []
for word in words:
    # Calculate vowelness score
    vowel_count = 0
    consonant_count = 0
    for letter in word:
        letter = letter.lower()
        if letter in "aeiou":
            vowel_count += 1
        elif letter in "abcdefghijklmnopqrstuvwxyz":
            consonant_count += 1
    score = vowel_count - consonant_count

    # Select color code
    if score >= 2:
        color_code = 35
    elif score >= 1:
        color_code = 34
    elif score >= 0:
        color_code = 36
    elif score >= -1:
        color_code = 32
    elif score >= -2:
        color_code = 33
    else:
        color_code = 31

    result_words.append("\033[%dm%s\033[0m" % (color_code, word))

result = " ".join(result_words)
print(result)
