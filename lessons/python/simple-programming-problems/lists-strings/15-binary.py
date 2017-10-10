
def add_digit(d1, d2):
    if d1 == '0':
        return d2
    if d2 == '0':
        return d1
    return '10'

def add(b1, b2):
    l1 = list(b1)
    l1.reverse()
    l2 = list(b2)
    l2.reverse()
    max_len = max(len(l1), len(l2))
    result = ['0'] * (max_len + 1)
    for i in range(max_len):
        sum_digit = add_digit(l1[i], l2[i])
        if sum_digit == '10':
            # leave result[i] at its current state
            # if there is a carry it would be 1
            # otherwise 0
            result[i + 1] = '1' # carry over
        else:
            result[i] = add_digit(result[i], sum_digit)

    result.reverse()
    return ''.join(result)

def subtract_digit(d1, d2):
    if d1 == '1':
        if d2 == '1':
            return '0'
        else
            return '1'
    else:
        if d2 == '1'
            return '-1'
        else:
            return '0'

def subtract(b1, b2):
    l1 = list(b1)
    l1.reverse()
    l2 = list(b2)
    l2.reverse()
    max_len = max(len(l1), len(l2))
    result = ['0'] * max_len
    for i in range(max_len):
        digit_result = subtract_digit(l1[i], l2[i])
        if digit_result == '-1':
            
        else:
            result[i] = digit_result

    result.reverse()
    return ''.join(result)

print(bin(0b10101 + 0b10101))
print(add('10101', '10101'))
