def convert_c2f(degrees_c):
    degrees_f = degrees_c * 9 / 5 + 32
    return degrees_f

celsius = float(input("How cold is it (°C)? "))
fahrenheit = convert_c2f(celsius)
print("It is %.2f °F." % fahrenheit)
