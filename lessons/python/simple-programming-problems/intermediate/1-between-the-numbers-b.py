current_combo   = [0, 0, 0, 0, 0, 0, 0, 0]
symbol_map = { 0: '-', 1: '+', 2: '' }
done = False
while not done:
    symbols = []
    for i in current_combo:
        symbols.append(symbol_map[i])
    result = None
    current_digits = '1'
    current_operator = None
    equation = '1'
    for i in range(len(symbols)):
        digit = str(i + 2)
        symbol = symbols[i]
        equation += symbol + digit
        if symbol == '-' or symbol == '+':
            number = int(current_digits)
            if current_operator is None:
                result = number
            elif current_operator == '+':
                result += number
            elif current_operator == '-':
                result -= number
            current_operator = symbol
            current_digits = digit
        elif symbol == '':
            current_digits += digit
        else:
            raise "This should not happen"
    number = int(current_digits)
    if current_operator is None:
        result = number
    elif current_operator == '+':
        result += number
    elif current_operator == '-':
        result -= number
    if result == 100:
        print("%s = %d" % (equation, result))
    i = 0
    while True:
        if i >= len(current_combo):
            done = True
            break
        current_combo[i] += 1
        if current_combo[i] > 2:
            current_combo[i] = 0
            i += 1
        else:
            break
