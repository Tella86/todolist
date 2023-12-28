tasks = []

def add_task(task):
    tasks.append({"task":task, "completed":False})
    print("Task added")

def list_tasks():
    print("\nTo-Do List")
    for index, task in enumerate(tasks, start=1):
        if task["completed"]:
            status = "✔"
        else:
            status = ""
        print(f"{index}. [{status}] {task['task']}")
    print()
    
def markcompleted(index):
   
        if 1 <= index <= len(tasks):
            tasks[index - 1]["completed"] = True
            print("Task marked as Complete")
        else:
            print("Invalid task Index")

def delete(task_index,tasks):
    if 1<= task_index <= len(tasks):
        print("Task Deleted Successfully")
    else:
        print("Invalid task index")
            

while True:
    print("\nOptions")
    print("1. Add a task")
    print("2. List tasks")
    print("3. Mark as  complete")
    print("4. Delete")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")
    
    if choice == "1":
        task = input("Enter the task:")
        add_task(task)

    elif choice == "2":
        list_tasks()

    elif choice == "3":
        list_tasks()
        index = int(input("Enter the task number: "))
        markcompleted(index)

    elif choice == "4":
        list_tasks()
        task_index= int((input("Enter the task index to delete: ")))
        delete(task_index,tasks)
        

    elif choice == "5":
        print("GoodBye")
        break
    else:
        print("Invalid choice. Please Choose 1, 2, 3, 4,or 5")


    

