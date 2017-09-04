number_of_pennies = 7
number_of_nickels = 4
number_of_dimes = 6
number_of_quarters = 5
number_of_one_dollar_bills = 4

total_amount = 0
total_amount += number_of_one_dollar_bills
total_amount += number_of_quarters * 0.25
total_amount += number_of_dimes * 0.1
total_amount += number_of_nickels * 0.05
total_amount += number_of_pennies * 0.01

print("I have %.2f dollars." % total_amount)
    