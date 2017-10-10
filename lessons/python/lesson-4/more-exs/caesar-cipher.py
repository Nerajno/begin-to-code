# The following 3 lines read the contents of the file secret-message.txt
# into the `text` variable.
file_handle = open('secret-message.txt')
text = file_handle.read()
file_handle.close()

# Implement the Caesar Cipher - using the key of 13 (the standard) to decipher
# the message.
#
# What is the Caesar Cipher? Read about it:
# http://practicalcryptography.com/ciphers/caesar-cipher/

print(text)
