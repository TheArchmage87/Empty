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
    y=1
    for x in tasks:
        print(str(y)+". "+x)
        y=y+1
    task_remove=input("Type the number of the task to remove or exit to return to main menu.")
    if task_remove=="exit" or task_remove=="Exit":
        pass
    else:
        task_remove=str(tasks[int(task_remove)-1])
        tasks.remove(task_remove)
        print(task_remove+" was removed from your To-Do list")
        time.sleep(1)
    display_menu()
def view_tasks():
    y=1
    print("To-Do List")
    for x in tasks:
        print(str(y)+". "+x)
        y=y+1
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
    if x=="1":
        add_task()
    elif x=="2":
        remove_task()
    elif x=="3":
        view_tasks()
    elif x=="4":
        end()
display_menu()