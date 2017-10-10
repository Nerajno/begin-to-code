current_combo   = [0, 0, 0, 0, 0, 0, 0, 0]
symbol_map = { 0: '-', 1: '+', 2: '' }
done = False
while not done:
    symbols = list(map(lambda i: symbol_map[i], current_combo))
    equation = '1'
    for i in range(len(symbols)):
        symbol = symbols[i]
        equation += symbol + str(i + 2)
    result = eval(equation)
    if result == 100:
        print(equation, '=', eval(equation))
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
