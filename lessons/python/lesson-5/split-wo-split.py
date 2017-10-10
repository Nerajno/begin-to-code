sentence = input('Enter a sentence: ')

new_word_list = []
current_word = ''
for char in sentence:
    if char == ' ':
        new_word_list.append(current_word)
        current_word = ''
    else:
        current_word = current_word + char

new_word_list.append(current_word)

print(new_word_list)
