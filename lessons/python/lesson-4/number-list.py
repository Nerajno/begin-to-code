number_list = []
while True:
    print('1. Add a number')
    print('2. Display the numbers')
    print('3. Display total')
    print('4. Display average')
    print('5. Display count')
    answer = input('What do you want to do? ')
    if answer == '1':
        number = input('Enter a number: ')
        number_list.append(float(number))
    elif answer == '2':
        print(number_list)
