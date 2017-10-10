sentence = input('Enter a sentence: ')

word_list = sentence.split(' ')
new_word_list = []

for word in word_list:
    reversed_word = ''
    for char in word:
        reversed_word = char + reversed_word
    new_word_list.append(reversed_word)

new_sentence = ' '.join(new_word_list)
print(new_sentence)
