def call_3_times(function):
    function()
    function()
    function()

def hello():
    print("Hello")

call_3_times(hello)

def call_3_times_with(fn, n):
    for i in range(3):
        fn(n)

def hello_you(you):
    print("Hello, %s!" % you)

call_3_times_with(hello_you, "John")
