sentence = input('Enter a sentence: ')

new_sentence = ''
digits = ''
collecting_digits = False

for char in sentence:
    if collecting_digits:
        if char in '0123456789':
            digits = digits + char
        else:
            collecting_digits = False
            number = int(digits) * 3
            new_sentence = new_sentence + str(number) + char
    else:
        if char in '0123456789':
            collecting_digits = True
            digits = char
        else:
            new_sentence = new_sentence + char

print(new_sentence)
