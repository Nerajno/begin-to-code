# Lesson 10
## Records

---
Hello!!! Welcome to class. Today we are going to talk about records.

*Note: Record is not a well-known term in the Python world. It's a term
that has many meanings and definitions in different contexts. I chose the
term for use within the context of this class.*

A Record is a special type of object --- which I created --- that is used
to store multiple pieces of information together. Every language has
something like this, and all of them use this "thing" extensively.

* JavaScript folks calls them objects
* Python people use objects or tuples - but we are using my "Record"
* C kin call them structs

With the ability to use records, you will also be able to start slicing and
dicing datasets, which is something you would be doing a lot on a daily basis
as a working developer.
********************************************************
## Prior Art

![Python Cookbook](lessons/python/lesson-10/images/python-cookbook.png)

---
I didn't completely come up with Records on my own. I learned it from
a co-worker a long time ago. But it turns out that the "Python Cookbook"
had covered this concept and implementation in their chapter 4.18 titled:
[Collecting a Bunch of Named Items](https://books.google.com/books?id=Q0s6Vgb98CQC&lpg=PT212&dq=Python+Cookbook+%22Collecting+a+Bunch+of+Named+Items%22&hl=en&pg=PT213#v=onepage&q&f=false). They actually called this concept a *bunch*.

********************************************************
## Record Definition

A record is an object that contains one or more attributes, each of which
can be accessed and modified. An attribute has a name and a value, and can
be used to store values of any type in Python.

---
This is the English-word definition of record.
********************************************************
## Record Code Definition

```python
class Record(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __repr__(self):
        return "Record%r" % self.__dict__
```

---
We will use this class definition for Record.
There is a lot to this code (we haven't even covered classes, LOL) ---
I understand it probably looks daunting to you, that's okay.
For now, **I will not explain how this works.** You are only concerned with
how to use a record, not how it works.

Just take this code as is --- copy this code and paste it at the beginning of
your code solutions that need to use records.
********************************************************
## Record: How to Create

```python
person = Record(name="Alice", age=7)
```

---
Now, assuming you have the record class defined at the beginning of your file,
you can use it like this to create a record that contains 2 *attributes*: name, and
age.

This record represents a person that has both a name and an age. The name
attribute, like a variable within the record, stores the value "Alice", and
the age attribute stores the value 7.
********************************************************
## Record: How to Create

```python
person = [[Record(name="Alice", age=7)]][[Constructor call: returns a new record]]
```

---
This expression which looks like a function call, is actually a
*constructor call*. A constructor is a function that creates a new
object and returns it. In this case, it returns a new record.
********************************************************
## Record: How to Create

```python
person = Record([[name="Alice", age=7]][[Named arguments]])
```

---
You might have notice that the arguments that are passed to `Record` look
a little different from what you are used to. These are *named arguments*.

*Named arguments* is another way to pass arguments to a function ---
they are not limited to constructors. I will hand-wave over how named arguments
work for now, because to connect it to the underlying machinery that makes
records work requires a big detour. Just know that the names of the arguments
you write become the names of the attributes in the record.
********************************************************
## Record: How to Create

```python
person = Record([[name]][[Argument/attribute name]]="Alice", age=7)
```

---
The name on the left-hand side of the `=` is the name of the argument,
and also the name of an attribute on the record to be created.
********************************************************
## Record: How to Create

```python
person = Record(name=[["Alice"]][[Argument/attribute value]], age=7)
```

---
The value on the right-hand side of the `=` is the value of the
argument, and also the value of the `name` attribute on the record to
be created.
********************************************************
## Record: How to Create

```python
person = Record(name="Alice", [[age]][[Argument/attribute name]]=7)
```

---
Similarly, `age` is another argument/attribute name,
********************************************************
## Record: How to Create

```python
person = Record(name="Alice", age=[[7]][[Argument/attribute value]])
```

---
and its value will be 7.
********************************************************
## Order Indifference

```python
person = Record(name="Alice", age=7)
```

same as

```python
person = Record(age=7, name="Alice")
```

---
Because the arguments are named, the constructor knows what each of them are
and the order in which you provide the arguments no longer matters.
********************************************************
## Record: How to Access

```python
print(person.name, "is", person.age, "years old.")
```

---
Once you have a record created, you can access its values.

As you might have guessed, this will print "Alice is 7 years old."
********************************************************
## Record: How to Access

```python
print([[person.name]][[dot notation]], "is", person.age, "years old.")
```

---
A record is an object (a type of object), and we are using the dot
notation to access an attribute on the record.

This is the same dot notation we use when we call a method
on a list object, say `my_list.append(3)`, except that the attribute we are
accessing is not a method that needs to be called using a set of `()`, it's
simply a string or number value --- or it could theoretically be any value.
********************************************************
## Record: How to Access

```python
print([[person.name]][[Gives "Alice"]], "is", person.age, "years old.")
```

---
So `person.name` gives us the value "Alice" --- as was previously defined,
********************************************************
## Record: How to Access

```python
print(person.name, "is", [[person.age]][[Gives 7]], "years old.")
```

---
And `person.age` gives us the value 7.
********************************************************
## Record: How to modify

```python
person.name = "Ally"
person.age = 8
```

---
You can change the value of an attribute in a record, just as easily as
assigning a new value to it using the `=` assignment operator.
********************************************************
## Record: How to modify

```python
[[person.name]][[lhs: an attribute of person]] = "Ally"
person.age = 8
```

---
In this case, the left-hand side of the `=` is no longer just a variable
name, as is the case for variable assignments. The left-hand side now is
an attribute of an object --- gotten using the dot operator.

In a sense, you can look at a record as a bag of variables --- each of its
attributes representing one variable within the bag.
********************************************************
## Create an Empty Record

```python
a_record = Record()
```

---
You can also create an empty record --- a record with no attributes, like so.
********************************************************
## Create an Empty Record

```python
a_record = Record()
a_record.city = "Atlanta"
a_record.temperature = 14
```

---
and then later, add attributes to it as you go.
********************************************************
## Create an Empty Record

```python
a_record = Record()
[[a_record.city = "Atlanta"]][[Adds a city attribute]]
a_record.temperature = 14
```

---
When you assign a value to an attribute, if that attribute
doesn't already exist on the record, it gets automatically added.
********************************************************
## Weather Example

```python
weather = Record()
weather.city = input("What city are you in? ")
weather.fahrenheit = float(input("What is the temperature °F in %s? " % weather.city))
weather.celsius = convert_f2c(weather.fahrenheit)
```

---
Assume the function `convert_f2c` has been defined, and it converts a
degree °F to °C.

[Run this in Python Tutor](http://pythontutor.com/visualize.html#code=class%20Record%28object%29%3A%0A%20%20%20%20def%20__init__%28self,%20**kw%29%3A%0A%20%20%20%20%20%20%20%20self.__dict__.update%28kw%29%0A%0A%20%20%20%20def%20__repr__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20%22Record%25r%22%20%25%20self.__dict__%0A%0Adef%20convert_f2c%28f%29%3A%0A%20%20%20%20return%20%28f%20-%2032%29%20*%205%20/%209%0A%0Aweather%20%3D%20Record%28%29%0Aweather.city%20%3D%20input%28%22What%20city%20are%20you%20in%3F%20%22%29%0Aweather.fahrenheit%20%3D%20float%28input%28%22What%20is%20the%20temperature%20%C2%B0F%20in%20%25s%3F%20%22%20%25%20weather.city%29%29%0Aweather.celsius%20%3D%20convert_f2c%28weather.fahrenheit%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%22Atlanta%22,%2214%22%5D&textReferences=false)
********************************************************
## Weather Example

![Weather record](lessons/python/lesson-10/images/weather-record.png)

---
This is what the `weather` record looked like at the end of the program run
in Python Tutor.

When you are in Python Tutor, a record instance looks like a table
with 2 columns. The attribute names are in the first column, and the attribute
values are in the second column, and as you run the program and change
the record, this table updates.
********************************************************
## Weather Example

```python
weather = Record()
weather.city = input("What city are you in? ")
weather.fahrenheit = float(input("What is the temperature °F in %s? " % weather.city))
weather.celsius = convert_f2c(weather.fahrenheit)
```

---
So, what is the point of using a record in this code?
********************************************************
## Weather Example

```python
city = input("What city are you in? ")
fahrenheit = float(input("What is the temperature °F in %s? " % city))
celsius = convert_f2c(fahrenheit)
```

---
We could have simply used normal variables, like this. Why bother at all
with records?
********************************************************
## Weather Example

```python
city = input("What city are you in? ")
fahrenheit = float(input("What is the temperature °F in %s? " % city))
celsius = convert_f2c(fahrenheit)
```

---
What if there are multiple cities, and we wanted to be able to go through
each city and print them out?
********************************************************
## Weather Example

```python
city1 = input("What city? ")
fahrenheit1 = float(input("What is the temperature °F in %s? " % city1))
celsius1 = convert_f2c(fahrenheit1)

city2 = input("What city? ")
fahrenheit2 = float(input("What is the temperature °F in %s? " % city2))
celsius2 = convert_f2c(fahrenheit2)

print("It's %.02d°C in %s" % (city1, celsius1))
print("It's %.02d°C in %s" % (city2, celsius2))
```

---
Okay, you can probably do something like this for 2 cities --- use a different
set of variables for each city using a naming convention. But what about 3
cities? 5 cities? What if you don't know beforehand how many cities there
will be?

Let's say the user can enter as many cities as he'd like. What do you do?

********************************************************
## Weather Example: Multiple Cities

```python
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
```

---
Records!!!

You use a while loop to let them enter another city indefinitely, and
add a new record to a list each time a city has been entered.
********************************************************
## Weather Example: Multiple Cities

```python
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
```

---
At the and of this while loop, the user might have entered 10, 50, even 100
city weather records!

[Run this code in Python Tutor](http://pythontutor.com/visualize.html#code=class%20Record%28object%29%3A%0A%20%20%20%20def%20__init__%28self,%20**kw%29%3A%0A%20%20%20%20%20%20%20%20self.__dict__.update%28kw%29%0A%0A%20%20%20%20def%20__repr__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20%22Record%25r%22%20%25%20self.__dict__%0A%0Adef%20convert_f2c%28f%29%3A%0A%20%20%20%20return%20%28f%20-%2032%29%20*%205%20/%209%0A%0Acities%20%3D%20%5B%5D%0Awhile%20True%3A%0A%20%20%20%20weather%20%3D%20Record%28%29%0A%20%20%20%20weather.city%20%3D%20input%28%22What%20city%3F%20%22%29%0A%20%20%20%20weather.fahrenheit%20%3D%20float%28input%28%22What%20is%20the%20temperature%20%C2%B0F%3F%20%22%29%29%0A%20%20%20%20weather.celsius%20%3D%20convert_f2c%28weather.fahrenheit%29%0A%20%20%20%20cities.append%28weather%29%0A%20%20%20%20yn%20%3D%20input%28%22Wanna%20add%20another%3F%20%28y%20or%20n%29%20%22%29%0A%20%20%20%20if%20yn%20!%3D%20%22y%22%3A%0A%20%20%20%20%20%20%20%20break%0A%0Aprint%28cities%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%22Atlanta%22,%2214%22,%22y%22,%22New%20York%22,%2213%22%5D&textReferences=false) and enter a couple of cities
to see records + lists in action.

********************************************************
## Lists of Records

```python
cities = [
    Record(city="Atlanta",   temperature=14),
    Record(city="London",    temperature=46.4),
    Record(city="Rome",      temperature=52.52),
    Record(city="New York",  temperature=17),
    Record(city="Cleveland", temperature=13)
]
```

---
Now that you've seen how to ask the user to enter a list of records. Let's
consider what you can do with a list of records, once you have access to them.

Let's stick to the weather theme, but we'll stop worrying about unit
conversion for the moment. We have a list of weather records, created in
Python like this --- although, this list could also have come from user
entry, a file, or a database.

What kind of questions can you answer about this dataset? Think of as many
as you can, and write them down before moving to the next slide.
********************************************************
## Questions You Can Answer

1. What is the temperature in _________?
2. Which cities are below freezing 32°F?
3. What is the coldest city?
4. What is the average temperature?

---
These are just some of the questions you can answer about the dataset,
by writing code. In fact, you can write a function to answer each one.

Look through each question and think about how you would solve each one.

We'll go through how to do each of these. If you are the type that
prefers to try to figure it out yourself, have a try before going
to the next slide.
********************************************************
## What is the temperature in _________?

```python
def temperature_in_city(target_city, records):
    for record in records:
        if record.city == target_city:
            return record.temperature
```

---
This function returns the temperature for a particular city.
********************************************************
## What is the temperature in _________?

```python
def temperature_in_city([[target_city]][[name of the city]], records):
    for record in records:
        if record.city == target_city:
            return record.temperature
```

---
It takes the name of the target city as a string.
********************************************************
## What is the temperature in _________?

```python
def temperature_in_city(target_city, [[records]][[list of records]]):
    for record in records:
        if record.city == target_city:
            return record.temperature
```

---
And it takes a list of records. Each record in the list contains
the attributes `city`, and `temperature`.
********************************************************
## What is the temperature in _________?

```python
def temperature_in_city(target_city, records):
    [[for record in records:]][[Loop through the records]]
        if record.city == target_city:
            return record.temperature
```

---
We are going to loop through the records, until we find one
that matches the city name we are looking for.
********************************************************
## What is the temperature in _________?

```python
def temperature_in_city(target_city, records):
    for record in records:
        [[if record.city == target_city:]][[Did we find match?]]
            return record.temperature
```

---
This if statement detects the record with the targeted city name
--- if one exists.
********************************************************
## What is the temperature in _________?

```python
def temperature_in_city(target_city, records):
    for record in records:
        if record.city == target_city:
            [[return record.temperature]][[return the temperature]]
```

---
If it matches, it returns that city's temperature. This return statement
has 2 effects:

1. return a value to the caller of the function
2. terminate this function immediately, which also has the effect of breaking
  out of this loop

That's right! The return statement can double as a break statement (for
  breaking out of a loop) when you are inside of a function.
********************************************************
## What is the temperature in _________?

```python
def temperature_in_city(target_city, records):
    for record in records:
        if record.city == target_city:
            return record.temperature
```

---
[Run this code in Python Tutor](http://pythontutor.com/visualize.html#code=class%20Record%28object%29%3A%0A%20%20%20%20def%20__init__%28self,%20**kw%29%3A%0A%20%20%20%20%20%20%20%20self.__dict__.update%28kw%29%0A%0A%20%20%20%20def%20__repr__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20%22Record%25r%22%20%25%20self.__dict__%0A%0A%0Arecords%20%3D%20%5B%0A%20%20%20%20Record%28city%3D%22Atlanta%22,%20%20%20temperature%3D14%29,%0A%20%20%20%20Record%28city%3D%22London%22,%20%20%20%20temperature%3D46.4%29,%0A%20%20%20%20Record%28city%3D%22Rome%22,%20%20%20%20%20%20temperature%3D52.52%29,%0A%20%20%20%20Record%28city%3D%22New%20York%22,%20%20temperature%3D17%29,%0A%20%20%20%20Record%28city%3D%22Cleveland%22,%20temperature%3D13%29%0A%5D%0A%0A%23%20What%20is%20the%20temperature%20in%20_________%3F%0Adef%20temperature_in_city%28target_city,%20records%29%3A%0A%20%20%20%20for%20record%20in%20records%3A%0A%20%20%20%20%20%20%20%20if%20record.city%20%3D%3D%20target_city%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20record.temperature%0A%0Aprint%28temperature_in_city%28%22Atlanta%22,%20records%29%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) to see this
in action.
********************************************************
## Which cities are below freezing 32°F?

```python
def cities_below_freezing(records):
    below_freezing = []
    for record in records:
        if record.temperature < 32:
            below_freezing.append(record.city)
    return below_freezing
```

---
Next is the problem of finding all cities that are below
freezing. This code uses a pattern. Do you recognize which one
it is?
********************************************************
## Which cities are below freezing 32°F?

```python
def cities_below_freezing(records):
    below_freezing = []
    for record in records:
        if record.temperature < 32:
            below_freezing.append(record.city)
    return below_freezing
```

---
That's right!!! It's the accumulator pattern ...
with filtering!
********************************************************
## Which cities are below freezing 32°F?

```python
def cities_below_freezing(records):
    [[below_freezing = []]][[collect all freezing cities here]]
    for record in records:
        if record.temperature < 32:
            below_freezing.append(record.city)
    return below_freezing
```

---
The accumulator variable is `below_freezing`. We are
appending to it the name of each city that is below freezing.
********************************************************
## Which cities are below freezing 32°F?

```python
def cities_below_freezing(records):
    below_freezing = []
    [[for record in records:]][[loop through the records]]
        if record.temperature < 32:
            below_freezing.append(record.city)
    return below_freezing
```

---
Again, we are looping through the records.
********************************************************
## Which cities are below freezing 32°F?

```python
def cities_below_freezing(records):
    below_freezing = []
    for record in records:
        [[if record.temperature < 32:]][[is it below freezing?]]
            below_freezing.append(record.city)
    return below_freezing
```

---
If the record has a temperature that is below freezing,
********************************************************
## Which cities are below freezing 32°F?

```python
def cities_below_freezing(records):
    below_freezing = []
    for record in records:
        if record.temperature < 32:
            [[below_freezing.append(record.city)]][[add that freezing city]]
    return below_freezing
```

---
we append the name of the city --- by accessing the `city` attribute
of the record --- to the `below_freezing` list.
********************************************************
## Which cities are below freezing 32°F?

```python
def cities_below_freezing(records):
    below_freezing = []
    for record in records:
        if record.temperature < 32:
            below_freezing.append(record.city)
    [[return below_freezing]][[Return frozen cities]]
```

---
Finally, we return all the frozen cities that we collected
in the process.
********************************************************
## Which cities are below freezing 32°F?

```python
def cities_below_freezing(records):
    below_freezing = []
    for record in records:
        if record.temperature < 32:
            below_freezing.append(record.city)
    return below_freezing
```

---
Please [run this in Python Tutor](http://pythontutor.com/visualize.html#code=class%20Record%28object%29%3A%0A%20%20%20%20def%20__init__%28self,%20**kw%29%3A%0A%20%20%20%20%20%20%20%20self.__dict__.update%28kw%29%0A%0A%20%20%20%20def%20__repr__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20%22Record%25r%22%20%25%20self.__dict__%0A%0A%0Arecords%20%3D%20%5B%0A%20%20%20%20Record%28city%3D%22Atlanta%22,%20%20%20temperature%3D14%29,%0A%20%20%20%20Record%28city%3D%22London%22,%20%20%20%20temperature%3D46.4%29,%0A%20%20%20%20Record%28city%3D%22Rome%22,%20%20%20%20%20%20temperature%3D52.52%29,%0A%20%20%20%20Record%28city%3D%22New%20York%22,%20%20temperature%3D17%29,%0A%20%20%20%20Record%28city%3D%22Cleveland%22,%20temperature%3D13%29%0A%5D%0A%0A%23%20Which%20cities%20are%20below%20freezing%2032%C2%B0F%3F%0Adef%20cities_below_freezing%28records%29%3A%0A%20%20%20%20below_freezing%20%3D%20%5B%5D%0A%20%20%20%20for%20record%20in%20records%3A%0A%20%20%20%20%20%20%20%20if%20record.temperature%20%3C%2032%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20below_freezing.append%28record.city%29%0A%20%20%20%20return%20below_freezing%0A%0Aprint%28cities_below_freezing%28records%29%29%0A&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false).
********************************************************
# What is the coldest city?

```python
def coldest_city(records):
    coldest = None
    for record in records:
        if coldest == None:
            coldest = record
        elif coldest.temperature > record.temperature:
            coldest = record
    return coldest.city
```

---
To solve the coldest city problem, we'll also use the accumulator
pattern.
********************************************************
# What is the coldest city?

```python
def coldest_city(records):
    [[coldest = None]][[accumulator variable]]
    for record in records:
        if coldest == None:
            coldest = record
        elif coldest.temperature > record.temperature:
            coldest = record
    return coldest.city
```

---
We'll use this variable: `coldest` to hold the record
of the coldest city. Initially we set it to the special value of `None`
--- which is the way to represent nothing in Python (other languages use
  null or nil).

As we iterate through the records, we'll update it with a colder city
each time we find a colder one in the list of records.
********************************************************
# What is the coldest city?

```python
def coldest_city(records):
    coldest = None
    [[for record in records:]][[loop through each record]]
        if coldest == None:
            coldest = record
        elif coldest.temperature > record.temperature:
            coldest = record
    return coldest.city
```

---
We'll again loop through each record.
********************************************************
# What is the coldest city?

```python
def coldest_city(records):
    coldest = None
    for record in records:
        [[if coldest == None:]][[no record yet]]
            coldest = record
        elif coldest.temperature > record.temperature:
            coldest = record
    return coldest.city
```
---
We use the `coldest == None` check to detect if we don't even have
a coldest record saved yet. This should happen the first time through this
loop because `None` is the value we initialized `coldest` to.
********************************************************
# What is the coldest city?

```python
def coldest_city(records):
    coldest = None
    for record in records:
        if coldest == None:
            [[coldest = record]][[update coldest]]
        elif coldest.temperature > record.temperature:
            coldest = record
    return coldest.city
```

---
In that case, we make the current record the coldest one.
This is in fact the coldest city we've seen so far --- out of 1.
********************************************************
# What is the coldest city?

```python
def coldest_city(records):
    coldest = None
    for record in records:
        if coldest == None:
            coldest = record
        [[elif coldest.temperature > record.temperature:]][[this one beats the coldest]]
            coldest = record
    return coldest.city
```

---
Otherwise, that means there is already a `coldest` record.

If the current record we are looking at beats the coldest we've
seen so far (in that it is smaller),
********************************************************
# What is the coldest city?

```python
def coldest_city(records):
    coldest = None
    for record in records:
        if coldest == None:
            coldest = record
        elif coldest.temperature > record.temperature:
            [[coldest = record]][[update coldest]]
    return coldest.city
```

---
then we'll also update the coldest record we've seen to the current one.
********************************************************
# What is the coldest city?

```python
def coldest_city(records):
    coldest = None
    for record in records:
        if coldest == None:
            coldest = record
        elif coldest.temperature > record.temperature:
            coldest = record
    [[return coldest.city]][[Return the coldest city name]]
```

---
Finally, after processing all the records this way, we
return the city name of the coldest record in the list.
********************************************************
# What is the coldest city?

```python
def coldest_city(records):
    coldest = None
    for record in records:
        if coldest == None:
            coldest = record
        elif coldest.temperature > record.temperature:
            coldest = record
    return coldest.city
```

---
[Run this example in Python Tutor](http://pythontutor.com/visualize.html#code=class%20Record%28object%29%3A%0A%20%20%20%20def%20__init__%28self,%20**kw%29%3A%0A%20%20%20%20%20%20%20%20self.__dict__.update%28kw%29%0A%0A%20%20%20%20def%20__repr__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20%22Record%25r%22%20%25%20self.__dict__%0A%0A%0Arecords%20%3D%20%5B%0A%20%20%20%20Record%28city%3D%22Atlanta%22,%20%20%20temperature%3D14%29,%0A%20%20%20%20Record%28city%3D%22London%22,%20%20%20%20temperature%3D46.4%29,%0A%20%20%20%20Record%28city%3D%22Rome%22,%20%20%20%20%20%20temperature%3D52.52%29,%0A%20%20%20%20Record%28city%3D%22New%20York%22,%20%20temperature%3D17%29,%0A%20%20%20%20Record%28city%3D%22Cleveland%22,%20temperature%3D13%29%0A%5D%0A%0A%23%20What%20is%20the%20coldest%20city%3F%0Adef%20coldest_city%28records%29%3A%0A%20%20%20%20coldest%20%3D%20None%0A%20%20%20%20for%20record%20in%20records%3A%0A%20%20%20%20%20%20%20%20if%20coldest%20%3D%3D%20None%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20coldest%20%3D%20record%0A%20%20%20%20%20%20%20%20elif%20coldest.temperature%20%3E%20record.temperature%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20coldest%20%3D%20record%0A%20%20%20%20return%20coldest.city%0A%0Aprint%28coldest_city%28records%29%29%0A&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) to see how it works.
********************************************************
## What is the average temperature?

Left as an exercise for you.

---
The problem of finding the average temperature we will leave
as an exercise for the reader --- homework is waiting for you.
********************************************************
## Implications

What can you do with records and lists?

---
So, that is a taste of using records and lists for you.

The implications of combining records and list is big. There are lots of
practical problems you can solve by using lists of records.

What can't you do with records and lists?
********************************************************
## Summary

* Records
* Create with set attributes and values
* Create an empty record
* Access an attribute
* Update an attribute
* Using records with lists!

---
This is what you've learned.

********************************************************
## Homework

[Homework!](https://gist.github.com/airportyh/7e6ebc0e7629f62d9e6ce842feae7b79)

---
This is your homework. Enjoy!
