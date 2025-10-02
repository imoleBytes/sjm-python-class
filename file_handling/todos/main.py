
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

tasks = [
    {"title": "go to the movies", "done": "True"}, 
    {"title": "wash clothes", "done": "False"},
      {"title": "do laundry", "done": "True"}, 
    {"title": "wash the house", "done": "False"},
      {"title": "go to the church", "done": "True"}, 
    {"title": "go to a friend's place", "done": "False"}  
] 

selections = """
    1.  Show Tasks
    2.  Add a Task
    3.  Edit a Task
    4.  Toggle Completion of a Task
    5.  Delete a Task
    6.  Quit
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
        print("Tasks added successfully!")
    elif choice == "3":
        while True:
            try:
                task_num = int(input(f"Select a Task Number to Edit: (1 - {len(tasks)})"))
                t = tasks[task_num-1]["title"]
                new = input(f"Change this: [{t}] to: ")
                tasks[task_num-1]["title"] = new
                print("editted successfully!")
                break
            except:
                print("enter a valid number")      
        
        ...
    elif choice == "4":
        ...
    elif choice == "5":
        ...
    elif choice == "6":
        print("Thank you for using this Program")
        exit()
    else:
        print("Invalid choic,please choose betwwen 1 - 6")
        
    
