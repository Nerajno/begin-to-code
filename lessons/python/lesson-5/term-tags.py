f = open('text.terml')
text = f.read()
f.close()

code_map = {
    'red': 91,
    'green': 92,
    'yellow': 93,
    'blue': 94,
    'purple': 95,
    'cyan': 96,
    'bg-red': 41,
    'bg-green': 42,
    'bg-yellow': 43,
    'bg-blue': 44,
    'bg-purple': 45,
    'bg-cyan': 46,
    'bg-grey': 47,
    'bg-white': 7,
    'bold': 1,
    'dim': 2,
    'underline': 4,
    'blink': 5
}

# text = '<bold>On the Awesomeness of the State Pattern</bold>'
output = ''
state = 'open' # can be open, read_tag_name,
               # in_tag, read_close_tag, read_close_tag_name

# axillary state variables:
tag_name = None
close_tag_name = None
for char in text:
    if state == 'open':
        if char == '<':
            state = 'read_tag_name'
            tag_name = ''
        else:
            output += char
    elif state == 'read_tag_name':
        if char == '>':
            state = 'in_tag'
            code = code_map[tag_name]
            output += '\033[%dm' % code
        else:
            tag_name += char
    elif state == 'in_tag':
        if char == '<':
            state = 'read_close_tag'
        else:
            output += char
    elif state == 'read_close_tag':
        if char == '/':
            state = 'read_close_tag_name'
            close_tag_name = ''
        else:
            raise Exception("\033[41mACCCCCCCK!\033[0m")
    elif state == 'read_close_tag_name':
        if char == '>':
            state = 'open'
            output += '\033[0m'
        else:
            close_tag_name += char

print(output)
