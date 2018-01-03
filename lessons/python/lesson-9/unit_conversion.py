print("***************************")
print("* Unit Conversion Program *")
print("***************************")

print("1. Convert Liters to Gallons")
print("2. Convert Kilometers to Miles")
print("3. Convert Kilograms to Pounds")

choice = input("Choose one: ")
if choice == "1":
    result = convert_liter_to_gallons(amount)
elif choice == "2":
    result = convert_kilometers_to_miles(amount)
elif choice == "3":
    result = convert_kilograms_to_pounds(amount)
else:
    raise Exception("Unknown choice %s" % choice)

amount = float(input("Enter amount: "))
print("Answer: %.2f" % result)
