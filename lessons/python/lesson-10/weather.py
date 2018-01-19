from record import Record

def convert_f2c(f):
    return (f - 32) * 5 / 9

cities = []
while True:
    weather = Record()
    weather.city = input("What city? ")
    weather.fahrenheit = float(input("What is the temperature °F? "))
    weather.celsius = convert_f2c(weather.fahrenheit)
    cities.append(weather)
    yn = input("Wanna add another? (y or n) ")
    if yn != "y":
        break

print(cities)
