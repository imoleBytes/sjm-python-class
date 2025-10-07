
def printTasks(tasks):
    print(f"TASKS{" "*91}DONE")
    print("-".center(100,"-"))
    for task in tasks:
        title = task["title"]
        done = task["done"]
        num_space = 100 - (len(title) + len(done))-8
        print(f"----{title}{" "* num_space}{done}----")
    
    print(f"Tasks: {len(tasks)}".center(100,"-"))

    
"""
Tasks
- Show Tasks 
- Add a Task
- Delete a task
- Edit a task
- Complete a task
- Quit
"""

def persistDATA(tasks):
    f = open("tasks.txt", "w")
    for task in tasks:
        line = f"{task["title"]},{task["done"]}\n"
        f.write(line)    
    
    f.close()


def populateTasks():
    tasks = []
    f = open("tasks.txt") 
    for line in f.readlines():
        title, done = line.split(",")
        done = done.strip("\n")
        task = {"title": title, "done": done}
        tasks.append(task)      

       
    f.close()
    return tasks

tasks = populateTasks()


selections = """
    1.  Show Tasks
    2.  Add a Task
    3.  Edit a Task
    4.  Complete a Task
    5.  Un-complete a task
    6.  Delete a Task
    7.  Quit
Select (1 - 6): """
while True:
    choice = input(selections)
    if choice == "1":
        print("** These are the tasks ***".center(100,"*"))
        printTasks(tasks)
        print("*" * 100)
        # print("**************************")
    elif choice == "2":
        task_title = input("Add a task: ")
        task = {"title": task_title, "done": "False"}
        tasks.append(task)
        persistDATA(tasks)
        print("Tasks added successfully!")
    elif choice == "3":
        while True:
            try:
                task_num = int(input(f"Select a Task Number to Edit: (1 - {len(tasks)})"))
                t = tasks[task_num-1]["title"]
                new = input(f"Change this: [{t}] to: ")
                tasks[task_num-1]["title"] = new
                persistDATA(tasks)
                print("editted successfully!")
                break
            except:
                print("enter a valid number")              
    elif choice == "4":
        task_num = int(input(f"Select a Task to complete: (1-{len(tasks)}): "))
        done = tasks[task_num-1]["done"]
        if done == "False":
            tasks[task_num-1]["done"] = "True"
            print("Task completed successfully!")
            persistDATA(tasks)
        else:
            print("Task has already been done!")
    elif choice == "5":
        task_num = int(input(f"Select a Task to uncomplete: (1-{len(tasks)}): "))        
        tasks[task_num-1]["done"] = "False"
        persistDATA(tasks)
        print("Task uncompleted successfully!")
        ...
    elif choice == "6":
        task_num = int(input(f"Select Task to delete: (1-{len(tasks)}): "))
        tasks.pop(task_num-1)
        persistDATA(tasks)
        print(f"Task {task_num} deleted!!")
      
    elif choice == "7":
        print("Thank you for using this Program")
        exit()
    else:
        print("Invalid choice, please choose betwwen 1 - 6")
        
    
