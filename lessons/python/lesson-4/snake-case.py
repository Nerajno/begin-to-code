sentence = input('Enter a sentence')

new_sentence = ''
for char in sentence:
    if char == ' ':
        new_sentence = new_sentence + '-'
    elif char in '.,':
        pass # means do nothing
    else:
        new_sentence = new_sentence + char

print(new_sentence)
