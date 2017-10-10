sentence = input('Enter a string: ')

current_letter = None
new_sentence = ''
for char in sentence:
    if char == current_letter:
        pass
    else:
        current_letter = char
        new_sentence += char

print(new_sentence)
