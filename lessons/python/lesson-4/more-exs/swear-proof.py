# The following 3 lines read the contents of the file carlin.txt - part
# of George Carlin's comedy routine - into the string variable `text`.

file_handle = open('carlin.txt')
text = file_handle.read()
file_handle.close()

# change the string in the text variable to replace swear words with substitute
# words - you can pick the substitute words you want to use.

print(text)
