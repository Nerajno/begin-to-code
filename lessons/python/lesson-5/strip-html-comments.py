# Strip out text within parantesis

text = input('Enter the text: ')

is_in_parans = False
new_text = ''
for char in text:
    if is_in_parans:
        if char == ')':
            is_in_parans = False
    else:
        if char == '(':
            is_in_parans = True
        else:
            new_text += char

print(new_text)
