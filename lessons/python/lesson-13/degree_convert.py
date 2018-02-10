def convert_c_to_f(c):
    return c * 9 / 5 + 32

c = float(input("How hot is it in °C? "))
f = convert_c_to_f(c)
print("%.02f°F is %.02f°C" % (f, c))
