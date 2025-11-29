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
 
# tasks = [
#     {"todo": "go to the movies", "done": False},
#     {"todo": "do laundry", "done": False},
#     {"todo": "read some books", "done": False},
#     {"todo": "go to the gym", "done": False}
# ]


def populateTasks():
    tsks = []
    f = open("db.csv")
    while True:
        line = f.readline().strip("\n")
        if line == "":
            break              
        line = line.split(" | ")
        todo = line[0]
        done = bool(int(line[1]))
        task = {"todo": todo, "done": done}
        tsks.append(task)
    f.close()
    
    return tsks


def persisData(tasks):
    # [
    #     {"todo": "go to the movies", "done": False},
    #     {"todo": "do laundry", "done": False},
    #     {"todo": "read some books", "done": False},
    #     {"todo": "go to the gym", "done": False}
    # ]
    
    f = open("db.csv", "w")
    for i in tasks:
        done_val = 0
        if i["done"] == False:
            done_val = 0
        else:
            done_val = 1
        t = f"{i["todo"]} | {done_val}\n"
        
        f.write(t)        
     
    f.close()   
    ...
        
    # "go to the movies | false"

 
tasks = populateTasks()

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
        persisData(tasks)
        print("Todo added successfully!")
    elif option == "3":
        try:            
            task_num = int(input("Enter the task number to complete: "))
            tasks[task_num-1]["done"] = True
            persisData(tasks)
            print(f"task {task_num} completed!")
        except IndexError:
            print(f"please there are only {len(tasks)} tasks in your task manager.")
            
        
    elif option == "4":
        task_num = int(input("Enter the task number to delete: "))
        tasks.pop(task_num-1)
        persisData(tasks)
        print(f"task {task_num} deleted successfully!")        
    elif option == "5":        
        break
    else:
        print("invalid option, please enter 1 - 5")

print("Thanks for using Task Manager, have a good day.")