# the following 3 lines read the contents of the file chicken-wings.txt into
# the string variable `text`.
file_handle = open('chicken-wings.txt')
text = file_handle.read()
file_handle.close()

num_of_people = int(input('How many people are you serving? '))

# Change the text of the recipe in the SERVES section and in the ingredients
# section to adjust for the number of people you are serving
#
# How to only modify the numbers in the ingredients and not the directions?
# Be creative.

print(text)
