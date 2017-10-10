phrase = 'I am a teapot short and stout'
word_list = []
current_word = ''
for char in phrase:
  if char == ' ':
    word_list.append(current_word)
    current_word = ''
  else:
    current_word = current_word + char
word_list.append(current_word)

print(word_list)
