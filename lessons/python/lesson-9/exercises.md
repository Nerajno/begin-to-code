# Lesson 9 Exercises

## Vowel Count

Write a `vowel_count(string)` function that counts the # of vowels for a given
string. It has one parameter:

1. `string` - the string to be counted

It has one return value: a number representing the number of vowels in the
string.

After you've written this function.
Write some extra code to test this function and verify that
it works properly.

## Price of the Ride

A carnival ride costs $12.00 for adults; $6 for kids (12 or under);
$7 for senior citizens (60 or older). You have to be at least 48 inches to
ride.

Write a function `price_of_the_ride(age, height)`. It has two parameters:

* `age` - a number representing the age of the person
* `height` - a number representing the height of the person

Its return value depends:

If they qualify to ride, it should return the cost of the ride as a number.
If they do not qualify to ride, the function should return `None`.

Write some extra code to test this function and verify that
it works properly.

## Calculate Tips

Write a `calculate_tip(amount, service)` function that calculates gives
the amount of the tip given the amount of the bill and the quality of the
service. It has two parameters:

1. `amount` - a number representing the amount of the bill
2. `service` - a string which can be one of "good", "fair", and "poor". For
good service, 20% tip should be given; for fair service, 15% tip should be
given; and for poor service, 10% tip should be given.

Return value: a number representing the tip amount.

After you've written this function.
Write some extra code to test this function and verify that
it works properly.

## Reverse a String

Write a `reverse_string(string)` function that reverses a string.
For example: "bananas" -> "sananab".

It has one parameter:

1. `string` - the string to be reversed

Return value: a string - the reversed version of the string passed in.

Write some extra code to test this function and verify that
it works properly.

## Reverse the Words

Write a `reverse_words(string)` function that reverses the words of a
sentence. For example: "to be or not to be" -> "be to not or be to".

It has one parameter:

1. `string` - the string containing the sentence

Return value: a string - the version of the sentence with its words reversed.
Write some extra code to test this function and verify that
it works properly.

## Unit Conversion

This is a program that helps you do unit conversion from metric to imperial
units:

```python
print("***************************")
print("* Unit Conversion Program *")
print("***************************")

print("1. Convert Liters to Gallons")
print("2. Convert Kilometers to Miles")
print("3. Convert Kilograms to Pounds")

choice = input("Choose one: ")
amount = float(input("Enter amount: "))

if choice == "1":
    result = convert_liter_to_gallons(amount)
elif choice == "2":
    result = convert_kilometers_to_miles(amount)
elif choice == "3":
    result = convert_kilograms_to_pounds(amount)

print("Answer: %.2f" % result)
```

The only problem is that it's missing some functions that it needs to do the
actual conversion:

* convert_liter_to_gallons
* convert_kilometers_to_miles
* convert_kilograms_to_pounds

Please write these functions --- adding them to the beginning of this program
--- to make this program work.
