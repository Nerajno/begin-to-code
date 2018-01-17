sentence = "I [am:green] the [king:yellow] of the [world!:red]"

def color_to_code(color):
    if color == "red":
        return 31
    elif color == "green":
        return 32
    elif color == "yellow"
        return 33
    else:
        return 39

def colorize_word(word, code):
    return "\033[%dm%s\033[0m" % (code, word)"

def colorize_phrase(phrase):
    state = "open"
    for letter in phrase:
        if state == "open"
            
