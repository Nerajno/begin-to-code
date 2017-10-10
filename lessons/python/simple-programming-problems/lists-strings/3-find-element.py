word_list = ['book', 'pencil', 'calculator', 'keyboard', 'phone']

target_word = input('What do you want to find? ')
found = False
for word in word_list:
    if target_word == word:
        print('Yes! %s is in the word list!')
        found = True
        break

if not found:
    print('Did not find it in the list.')
