phrase = input("Write a phrase: ")

words = phrase.split(" ")
result_words = []
for word in words:
    reversed_word = ""
    for letter in word:
        reversed_word = letter + reversed_word
    result_words.append(reversed_word)

result = " ".join(result_words)
print(result)
