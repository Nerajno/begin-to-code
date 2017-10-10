sentence = input('Enter a sentence: ')
word_list = sentence.split(' ')
new_word_list = []
for word in word_list:
    if str.isdigit(word):
        number = int(word)
        new_word_list.append(str(number * 3))
    else:
        new_word_list.append(word)

new_sentence = " ".join(new_word_list)

print(new_sentence)
