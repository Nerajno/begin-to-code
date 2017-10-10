sentence = input('Enter sentence: ')

new_sentence = ''
all_caps_mode = False
for char in sentence:
    if all_caps_mode:
        if char == '!':
            all_caps_mode = False
        else:
            new_sentence += char.upper()
    else:
        if char == '!':
            all_caps_mode = True
        else:
            new_sentence += char

print(new_sentence)
