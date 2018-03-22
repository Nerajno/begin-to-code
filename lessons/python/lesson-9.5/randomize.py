import random

def randomize_letters(word):
    letters = list(word)
    for i in range(len(letters)):
        x = random.randint(0, len(letters) - 1)
        y = random.randint(0, len(letters) - 1)
        letters[x], letters[y] = letters[y], letters[x]
    return "".join(letters)

scores = [8, 3, 5, 2, 9, 5]

# sum, average and then standard deviation

print(randomize_letters("bananas"))
print(randomize_words("what the heck dude"))
