from record import Record

records = [
    Record(city="Atlanta",   temperature=14),
    Record(city="London",    temperature=46.4),
    Record(city="Rome",      temperature=52.52),
    Record(city="New York",  temperature=17),
    Record(city="Cleveland", temperature=13)
]

# What is the temperature in _________?
def temperature_in_city(target_city, records):
    for record in records:
        if record.city == target_city:
            return record.temperature

# print(temperature_in_city("Atlanta", records))

# Which cities are below freezing 32°F?
def cities_below_freezing(records):
    below_freezing = []
    for record in records:
        if record.temperature < 32:
            below_freezing.append(record.city)
    return below_freezing

print(cities_below_freezing(records))

# What is the coldest city?
def coldest_city(records):
    coldest = None
    for record in records:
        if coldest == None:
            coldest = record
        elif coldest.temperature > record.temperature:
            coldest = record
    return coldest.city

# What is the average temperature?
def average_temperature(records):
    total_temperature = 0
    for record in records:
        total_temperature += record.temperature
    return total_temperature / len(records)
