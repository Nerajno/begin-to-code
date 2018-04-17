# JS Lesson 6 Exercises

For the form problems below, make sure you register for the form submit
event and prevent default.

## Tip Calculator

Make a tip calculator form. This form has:

1. A label and a text input for the user to enter the total amount.
2. A select box for the user to choose between 10%, 15%, and 20%.
3. A submit button.

Make it so that when the submit button is clicked, a tip amount
as well as a total amount are displayed underneath the form.

## Caesar Cipher Converter

Write a Caesar Cipher Converter form. This form has:

1. A text area for the user to enter either original text or cipher text.
2. Two radio buttons --- encode vs decode --- for them to select either to encode the text, or to decode
the text (use the offset of 13).
3. A checkbox for the user to specify whether to preserve capitalization of
words.
4. A "convert" button.

When the convert button is clicked, the converted text will be displayed
beneath the form.

## Smoothies

Write a smoothie order form. The order form has:

1. A select box containing the 5 available smoothie flavors: strawberry-banana,
orange-mango, lemonade, crazy berries, chocolate.
2. Three radio buttons --- small, medium, large --- for them to select
the smoothie size.
3. An "Add Smoothie" button.
(This button should *not* have the attribute `type="submit"`)
4. A `ul` list element containing the currently selected smoothies in the order.
4. A "Place Order" button.

Each time "Add Smoothie" is clicked, a new `li` containing the details about
the smoothie is added to the selected smoothies list.
