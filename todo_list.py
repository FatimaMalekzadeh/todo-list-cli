# It saves the list of all tasks
tasks = []

# Four function have been created to allow user to
# perform the following tasks:

# ***show tasks list***
def show_tasks(tasks) :
    for i in tasks :
        if i["done"] :
            print(f'[X] {i["task"]}')
        else :
            print(f'[ ] {i["task"]}')

# ***add new task***
def add_task(tasks) :
    new_task = input("What task do you want to add? ")
    task_dict = {"task" : new_task, "done" : False}
    tasks.append(task_dict)

# ***deleting a task***
def remove_task(tasks) :
    new_number = int(input("Which number do you want to remove? "))
    real_index = (new_number - 1)
    tasks.pop(real_index)

# ***ticking off a task***
def mark_done(tasks) :
    new_number = int(input("Which number is done? "))
    real_index = (new_number - 1)
    tasks[real_index]["done"] = True

# ***main loop***
choice = 0
while choice != 5 :
    print("1.Show tasks")
    print("2.Add task")
    print("3.Remove a task")
    print("4.Mark a task as done")
    print("5.Exit")

    choice = int(input("What do you want to do? "))

    if choice == 1 :
        show_tasks(tasks)
    
    elif choice == 2 :
        add_task(tasks)

    elif choice == 3 :
        remove_task(tasks)

    elif choice == 4 :
        mark_done(tasks)

    elif choice == 5 :
        print("Good luck, Bye!")
