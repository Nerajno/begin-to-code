phrase = input('Enter a phrase: ')

word_list = phrase.split(' ')
new_word_list = []
for word in word_list:
    capitalized_word = word[0].upper() + word[1:]
    new_word_list.append(capitalized_word)

new_phrase = ''.join(new_word_list)
print(new_phrase)
