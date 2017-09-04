pizza_price = 18.00
bread_stick_price = 5.00

number_of_pizzas = 2
number_of_bread_sticks = 3

total_pizza_price = pizza_price * number_of_pizzas
total_bread_stick_price = bread_stick_price * number_of_bread_sticks

total_price = total_pizza_price + total_bread_stick_price

discount = 0.20

total_price = total_price * (1.00 - discount)

number_of_people_paying = 4
total_per_person = total_price / number_of_people_paying

print('Each person pays $%.2f.' % total_per_person)