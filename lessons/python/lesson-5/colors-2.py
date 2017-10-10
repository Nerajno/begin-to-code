the_input = '*Today* I am [very happy] about my (coffee).'

colored_output = ''
state = 'open' # can be 'open', 'red', 'green' or 'purple'
for char in the_input:
    if state == 'open':
        if char == '*':
            state = 'red'
            colored_output += '\033[91m'
        elif char == '[':
            state = 'green'
            colored_output += '\033[92m'
        elif char == '(':
            state = 'purple'
            colored_output += '\033[95m'
        else:
            colored_output += char
    elif state == 'red':
        if char == '*':
            state = 'open'
            colored_output += '\033[0m'
        else:
            colored_output += char
    elif state == 'green':
        if char == ']':
            state = 'open'
            colored_output += '\033[0m'
        else:
            colored_output += char
    elif state == 'purple':
        if char == ')':
            state = 'open'
            colored_output += '\033[0m'
        else:
            colored_output += char

print(colored_output)
