sentence = input('Enter a sentence: ')
word_list = sentence.split(' ')
new_word_list = []
for word in word_list:
    last_idx = len(word) - 1
    new_word = word[1:] + word[0] + 'ay'
    new_word_list.append(new_word)

new_sentence = " ".join(new_word_list)
print(new_sentence)
