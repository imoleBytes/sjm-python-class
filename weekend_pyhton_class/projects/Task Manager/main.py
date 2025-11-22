"""
PROGRAM NAME: TASK MANAGER
VERSION: 1.0.0
AUTHOR: IMOLE
CONTRIBUTOR: KAZEEM
LICENCE: MIT-LICENSE
DESCRIPTION: THIS IS A TASK MANAGER
"""

userName = "Imole"

# def displayPrompt():
prompt = f"""
Welcome to Task Manager, {userName}
\t1. Show tasks
\t2. Add a task
\t3. Complete a task
\t4. Delete a task
\t5. Quit"""
 
tasks = [
    {"todo": "go to the movies", "done": False},
    {"todo": "do laundry", "done": False},
    {"todo": "read some books", "done": False},
    {"todo": "go to the gym", "done": False}
]

def printFormattedTasks(todos):
    if len(todos) == 0:
        print("There are no tasks currently, please add a task...")
    else:    
        count = 1
        print("No.  |   Todo                   | Completed")
        for i in todos:
            print(f"{count}     | {i["todo"]}                   {i["done"]}")
            count += 1

while True:    
    print(prompt)
    option = input("Enter Option (1-5): ")
    if option == "1":
        printFormattedTasks(tasks)
    elif option == "2":
        title = input("Enter the task to add: ")
        todo = {"todo": title, "done": False}
        tasks.append(todo)
        print("Todo added successfully!")
    elif option == "3":
        try:            
            task_num = int(input("Enter the task number to complete: "))
            tasks[task_num-1]["done"] = True
            print(f"task {task_num} completed!")
        except IndexError:
            print(f"please there are only {len(tasks)} tasks in your task manager.")
            
        
    elif option == "4":
        task_num = int(input("Enter the task number to delete: "))
        tasks.pop(task_num-1)
        print(f"task {task_num} deleted successfully!")        
    elif option == "5":        
        break
    else:
        print("invalid option, please enter 1 - 5")

print("Thanks for using Task Manager, have a good day.")