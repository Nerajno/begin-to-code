from record import Record

def print_tasks(tasks):
    for idx in range(len(tasks)):
        num = idx + 1
        task = tasks[idx]
        check = " "
        if task.done:
            check = "x"
        print("%d. [%s] %s" % (num, check, task.name))

def print_menu():
    print("What do you want to do?")
    print("a. Add a task")
    print("b. Check-off a task")

tasks = []

while True:
    print_tasks(tasks)
    print_menu()
    choice = input("> ")
    if choice == "a":
        task = input("What is the task? ")
        tasks.append(Record(name=task, done=False))
    elif choice == "b":
        print_tasks(tasks)
        num = int(input("Which task to check-off? "))
        idx = num - 1
        tasks[idx].done = True
