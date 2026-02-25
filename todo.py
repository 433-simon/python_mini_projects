# In - Memory :
# defining all necessary functions
tasks = []
def add_task():
    while True: 
        task_name = input("Enter task name : ")
        task_priority = input("Categorzie task as priority (high/low/medium) : ")
        task_status = input("Enter your task status (pending/completed) : ")
        task_due_date = input("Enter your due date in form (DD/MM) : ")
        task_category = input("Enter task category i.e (work/personal/learning) : ")

        task = {
            "name" : task_name,
            "priority" : task_priority,
            "status" : task_status,
            "due_date" : task_due_date,
            "category" : task_category
        }

        tasks.append(task)
        print("Task Added Successfully!")

        option = input("do you want to add more tasks : ")
        if option.lower() != "yes" :
            print("tell what you wnat to do :")
            ask = input("show menu/ exit : ").strip().lower()
        if ask == "exit":
            exit_task()
        else:
            break


def update_task():
    print("update task selected")
    if not tasks:
        print("No task to update")
        return
    name = input("Enter name of Task you want to update : ").strip().lower()

    for task in tasks:
        if task["name"].lower() == name:
            tasks_status = input("Update your task status (complete/pending): ").strip().lower()

            if tasks_status in ["complete", "completed", "pending"]:
                task["status"] = tasks_status
                print("Task Updated Successfully!")
            else:
                print("Invalid status entered.")

            return

    print("Task not found.")


def view_task():
    print("View Task Selected")

    if not tasks:
        print("No Tasks available.")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']} | {task['priority']} | {task['status']} | Due: {task['due_date']} | Category: {task['category']}")


def delete_task():
    print("Delete Task Selected")
    if not tasks :
        print("No Tasks Availabe to Delete")
        return
    name = input("Enter name of task which you want to delete : ").strip().lower()
    for task in tasks:
        if task["name"].lower() == name:
            tasks.remove(task)
            print("Task Deleted Successfully!")
            return
        
    print("Task Not Found")

def exit_task():
    print("Exiting...task")
    quit()


def program_menu():
    print('''
1. Add Task 
2. Update Task
3. View Current Tasks
4. Delete Existing Tasks
5. Exit....'''
)
    choice = input("Enter your choice : ")
    menu_actions = {
        "1" : add_task,
        "2" : update_task,
        "3" : view_task,
        "4" : delete_task,
        "5" : exit_task 
    }
    action = menu_actions.get(choice)
    if action:
        action()
    else:
        print("Invalid choice")



print("Welcome to To-Do")

while True : 
    program_menu()
   

