# Lesson 10
## Records

---
Hello!!! Welcome to class. Today we are going to talk about records.
A record is a special object that is used to store multiple pieces
of information about a concept. Although different languages call it by
different names, all of them use it extensively.
********************************************************
## Record Definition

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
you can use it like this to create a record that contains 2 attributes: name, and
age.

This record represents a person that has both a name and an age. The name
attribute, like a variable within the record, stores the value "Alice", and
the age attribute stores the value 7.
********************************************************
## Record: How to Create

```python
person = [[Record(name="Alice", age=7)]][[Constructor call]]
```

---
This expression which looks like a function call, is actually a
constructor call --- which constructs a new record.
********************************************************
## Record: How to Create

```python
person = Record([[name="Alice", age=7]][[Named arguments]])
```

---
You might have notice that the arguments that are passed to the constructor
call are not like the arguments we pass to normal function calls. These
are called named arguments.

Named arguments is another way to pass arguments to a function, or constructor.
********************************************************
## Record: How to Create

```python
person = Record([[name]][[Argument name]]="Alice", age=7)
```

---
The name on the left-hand side of the equals sign is the name of the argument.
********************************************************
## Record: How to Create

```python
person = Record(name=[["Alice"]][[Argument value]], age=7)
```

---
And the value on the right-hand side of the equals sign is the value of the
argument.
********************************************************
## Record: Order Indifference

```python
person = Record(name="Alice", age=7)
```

same as

```python
person = Record(age=7, name="Alice")
```

---
Because the arguments are named, the constructor know what each of them are
and the order in which you provide the arguments no longer matters.
********************************************************
## Record: How to Access

```python
print(person.name, "is", person.age, "years old.")
```

---
Now that you have a record created, you can access its values.

As you might have guessed, this will print "Alice is 7 years old."
********************************************************
## Record: How to Access

```python
print([[person.name]][[dot notation]], "is", person.age, "years old.")
```

---
A record is an object, and we are using the dot notation to access an attribute
on the record.

This is the same dot notation we use when we call a method
on a list object, say `my_list.append(3)`, except that the attribute we are
accessing is not a method that needs to be called, it's simply a string
or number value.
********************************************************
## Record: How to modify
