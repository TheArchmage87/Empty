import time
tasks=[]
list_length=0
y=1
def add_task():
    print("Type task or type exit to return to menu.")
    task_add=input("")
    if task_add=="exit" or task_add=="Exit":
        display_menu()
    else:
        tasks.append(task_add)
        print(task_add+" was added to your To-Do list")
        time.sleep(1)
        display_menu()
def remove_task():
    for x in tasks:
        print(y+". "+x)
        y=y+1
    y=input("Type the number of the task to remove or exit to return to main menu.")
    if task_add=="exit" or task_add=="Exit":
        pass
    else:
        tasks.remove(int(y))
    y=1
    display_menu()
def view_tasks():
    for x in tasks:
        print(y+". "+x)
        y=y+1
    y=1
    input("Press Enter to return to Main Menu.")
    display_menu()
def end():
    print("Bye")
    time.sleep(2)
def display_menu():
    print("To-Do List Menu:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View all tasks")
    print("4. Exit")
    x=input("")
    if x==1:
        add_task()
    elif x==2:
        remove_task()
    elif x==3:
        view_task()
    elif x==4:
        end()
display_menu()