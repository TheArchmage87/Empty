tasks=[]
list_length=0
def add_task():
    print("Type task or type exit to return to menu.")
    task_add=input("")
    if task_add=="exit" or task_add=="Exit":
        display_menu()
def display_menu():
    print("To-Do List Menu:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View all tasks")
    print("4. Exit")
    x=input("")
    if x==1:
        add_task()
display_menu()