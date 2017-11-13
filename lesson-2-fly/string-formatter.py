name = input("Hello, what's your name? ")
age = int(input("How old are you? "))
milk = float(input("How many gallons of milk? "))
# print("Hello,", name, "!!!")
print("Hello %s!!! You are %d." % (name, age))
# print("You drink %f gallons of milk." % milk)
print("You drink %.2f gallons of milk." % milk)

# Terms
# "Hello %s!!!" - format string
# %s - string argument specifier
# %d - number w/o decimal points
# %f - number with decimal points
# %.2f - display number rounded to 2 decimal points
# name - one argument
# (name, age) - multiple arguments
# % - formatting operator
